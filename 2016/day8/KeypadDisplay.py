import cv2
from mock import patch
import numpy as np
from numpy import testing as nptest
import unittest


class TestKeypadDisplay(unittest.TestCase):
    def setUp(self):
        self.keypad = KeypadDisplay((3, 7))
        self.testDisplay = np.zeros((3, 7))

    def test_rectOperation(self):
        self.keypad.rect(3, 2)
        self.testDisplay[:2, :3] = 1
        nptest.assert_array_equal(self.testDisplay, self.keypad.display)

    def test_rotateColAfterRect(self):
        self.testDisplay[:2, 0] = 1
        self.testDisplay[1:, 1] = 1
        self.testDisplay[:2, 2] = 1
        self.keypad.rect(3, 2)
        self.keypad.rotate('col', 1, 1)
        nptest.assert_array_equal(self.testDisplay, self.keypad.display)

    def test_rotateRowAfterColAndRect(self):
        self.testDisplay[1, :3] = 1
        self.testDisplay[0, 4] = 1
        self.testDisplay[0, 6] = 1
        self.testDisplay[2, 1] = 1
        self.keypad.rect(3, 2)
        self.keypad.rotate('col', 1, 1)
        self.keypad.rotate('row', 0, 4)
        nptest.assert_array_equal(self.testDisplay, self.keypad.display)


class TestInstructionParser(unittest.TestCase):
    def setUp(self):
        self.keypad = KeypadDisplay((3, 7))
        self.parser = InstructionParser(self.keypad)

    def test_ParseRect(self):
        with patch.object(self.keypad, 'rect') as mock:
            self.parser.parse('rect 3x2')
        mock.assert_called_with(3, 2)

    def test_ParseRotate(self):
        with patch.object(self.keypad, 'rotate') as mock:
            self.parser.parse('rotate column x=1 by 1')
        mock.assert_called_with('col', 1, 1)


class KeypadDisplay:
    def __init__(self, dimensions=(6, 50)):
        self.display = np.zeros(dimensions)

    def rect(self, A, B):
        self.display[:B, :A] = 1

    def rotate(self, direction, index, shift):
        if direction == 'col':
            self.display[:, index] = np.roll(self.display[:, index], shift)
        elif direction == 'row':
            self.display[index, :] = np.roll(self.display[index, :], shift)


class InstructionParser:
    def __init__(self, keypad):
        self.keypad = keypad

    def parse(self, string):
        if 'rect' in string:
            rectSize = string.split(' ')[1].split('x')
            self.keypad.rect(int(rectSize[0]), int(rectSize[1]))
        elif 'rotate' in string:
            if 'col' in string:
                direction = 'col'
            else:
                direction = 'row'
            index = int(string.split('=')[1].split(' ')[0])
            shift = int(string.split('=')[1].split('by ')[1])
            self.keypad.rotate(direction, index, shift)


class TestInstructionGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = InstructionGenerator()
        self.keypad = KeypadDisplay((1, 9))
        self.parser = InstructionParser(self.keypad)

    def test_RowIsCorrectlyGenerated(self):
        testRow = np.array([0, 0, 1, 0, 1, 1, 0, 1, 1])
        self.generator.generateRowInstructions(testRow)
        for instruction in self.generator.instructions:
            self.parser.parse(instruction)
        nptest.assert_array_equal(np.array([testRow]), self.keypad.display)

    def test_InstructionGeneration(self):
        self.keypad.display = np.zeros((3, 7))
        testArray = np.array([[0, 1, 0, 0, 1, 0, 1],
                              [1, 0, 1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0]])
        self.generator.generateInstructionsRowByRowAndShiftRowsDown(testArray)
        for instruction in self.generator.instructions:
            self.parser.parse(instruction)
        nptest.assert_array_equal(testArray, self.keypad.display)


class InstructionGenerator:
    def __init__(self):
        self.instructions = []

    def generateRowInstructions(self, row):
        row = row[::-1]
        i = 0
        while i < len(row):
            onPixels = 0
            offPixels = 0
            while row[i] == 0:
                offPixels += 1
                i += 1
                if i == len(row):
                    break
            if i < len(row):
                while row[i] == 1:
                    onPixels += 1
                    i += 1
                    if i == len(row):
                        break
            self.instructions.append(''.join(['rotate row y=0 by ', str(onPixels + offPixels)]))
            if onPixels > 0:
                self.instructions.append(''.join(['rect ', str(onPixels), 'x1']))

    def generateInstructionsRowByRowAndShiftRowsDown(self, rows):
        rowCount = rows.shape[0]
        for row in rows[::-1]:
            self.generateRowInstructions(row)
            if rowCount > 1:
                for i in range(len(row)):
                    self.instructions.append(''.join(['rotate column x=', str(i), ' by 1']))
            rowCount -= 1


if __name__ == '__main__':
    keypad = KeypadDisplay()
    parser = InstructionParser(keypad)
    with open('input', 'r') as f:
        for line in f:
            parser.parse(line)
            cv2.imshow('keypad', cv2.resize(keypad.display, None, fx=20, fy=20, interpolation=cv2.INTER_CUBIC))
            cv2.waitKey(100)
    print 'Part 1: ', np.sum(keypad.display)
    cv2.imshow('keypad', cv2.resize(keypad.display, None, fx=20, fy=20, interpolation=cv2.INTER_CUBIC))
    cv2.waitKey(1000)
    generator = InstructionGenerator()
    reverseInput = np.zeros((7, 18))
    reverseInput[1:-1, 1] = 1
    reverseInput[3, 2] = 1
    reverseInput[1:-1, 3] = 1
    reverseInput[1:-1, 5] = 1
    reverseInput[1, 6] = 1
    reverseInput[3, 6] = 1
    reverseInput[5, 6] = 1
    reverseInput[1:-1, 8] = 1
    reverseInput[5, 9] = 1
    reverseInput[1:-1, 11] = 1
    reverseInput[5, 12] = 1
    reverseInput[1:-1, 14:17] = 1
    reverseInput[2:-2, 15:16] = 0

    generator.generateInstructionsRowByRowAndShiftRowsDown(reverseInput)
    for instruction in generator.instructions:
        parser.parse(instruction)
        cv2.imshow('keypad', cv2.resize(keypad.display, None, fx=20, fy=20, interpolation=cv2.INTER_CUBIC))
        cv2.waitKey(50)
    cv2.imshow('keypad', cv2.resize(keypad.display, None, fx=20, fy=20, interpolation=cv2.INTER_CUBIC))
    cv2.waitKey(0)
