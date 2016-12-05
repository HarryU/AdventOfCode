import numpy as np
import unittest


class TestKeyCodeFinder(unittest.TestCase):
    def setUp(self):
        pass

    def test_StartKeyIs5(self):
        keycodes = KeyCodeFinder()
        self.assertEqual(5, keycodes.getCurrentKey())

    def test_OneUpMovesTo2(self):
        keycodes = KeyCodeFinder()
        keycodes.move('U')
        self.assertEqual(2, keycodes.getCurrentKey())

    def test_OneDownMovesTo8(self):
        keycodes = KeyCodeFinder()
        keycodes.move('D')
        self.assertEqual(8, keycodes.getCurrentKey())

    def test_OneLeftMovesTo4(self):
        keycodes = KeyCodeFinder()
        keycodes.move('L')
        self.assertEqual(4, keycodes.getCurrentKey())

    def test_OneRightMovesTo6(self):
        keycodes = KeyCodeFinder()
        keycodes.move('R')
        self.assertEqual(6, keycodes.getCurrentKey())


class KeyCodeFinder:
    def __init__(self):
        self.keys = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.x = 1
        self.y = 1

    def getCurrentKey(self):
        return self.keys[self.y, self.x]

    def move(self, direction):
        if direction == 'U':
            self.y = max(self.y - 1, 0)
        if direction == 'D':
            self.y = min(self.y + 1, 2)
        if direction == 'L':
            self.x = max(self.x - 1, 0)
        if direction == 'R':
            self.x = min(self.x + 1, 2)


class Part2KeyCodeFinder:
    def __init__(self):
        self.keys = np.array([[None, None,  1, None,  None],
                              [None,  2,    3,   4,   None],
                              [  5,   6,    7,   8,    9  ],
                              [None, 'A',  'B', 'C',  None],
                              [None, None, 'D', None, None]])
        self.x = 0
        self.y = 2

    def getCurrentKey(self):
        return self.keys[self.y, self.x]

    def move(self, direction):
        if direction == 'U':
            self.y = max(self.y - 1, 0)
            if self.keys[self.y, self.x] is None:
                self.y += 1
        if direction == 'D':
            self.y = min(self.y + 1, 4)
            if self.keys[self.y, self.x] is None:
                self.y -= 1
        if direction == 'L':
            self.x = max(self.x - 1, 0)
            if self.keys[self.y, self.x] is None:
                self.x += 1
        if direction == 'R':
            self.x = min(self.x + 1, 4)
            if self.keys[self.y, self.x] is None:
                self.x -= 1


if __name__ == '__main__':
    finder = KeyCodeFinder()
    finderPart2 = Part2KeyCodeFinder()
    keycode = []
    part2KeyCode = []

    with open('input', 'r') as f:
        for line in f:
            line = line.strip('\n')
            for char in line:
                finder.move(char)
                finderPart2.move(char)
            keycode.append(finder.getCurrentKey())
            part2KeyCode.append(finderPart2.getCurrentKey())
    print 'Part 1:', keycode
    print 'Part 2:', part2KeyCode
