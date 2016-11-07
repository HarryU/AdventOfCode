import CharacterCounting
import unittest


class TestCharCounting(unittest.TestCase):
    def setUp(self):
        self.testInput = open('input.txt', 'r')

    def test_CountCharsOfCode(self):
        with open('testInput.txt', 'r') as testInput:
            self.assertEqual(2, CharacterCounting.charsOfCode(testInput.readline()))

    def test_CountCharsInEvaluatedString(self):
        with open('testInput.txt', 'r') as testInput:
            self.assertEqual(0, CharacterCounting.charsInString(testInput.readline()))

    def test_CharsOfCodeMinusCharsInString(self):
        code = 0
        string = 0
        for line in self.testInput:
            code += CharacterCounting.charsOfCode(line)
            string += CharacterCounting.charsInString(line)
        self.assertEqual(4845, string)
        self.assertEqual(1350, code - string)
