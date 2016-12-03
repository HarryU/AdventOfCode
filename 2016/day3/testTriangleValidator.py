import itertools
import unittest


class TestTriangleValidator(unittest.TestCase):
    def setUp(self):
        self.validator = TriangleValidator()

    def test_FiveTenTwentyFiveIsInvalid(self):
        self.assertFalse(self.validator.IsTriangleValid([5, 10, 25]))

    def test_ThreeFourFiveIsValid(self):
        self.assertTrue(self.validator.IsTriangleValid([3, 4, 5]))

    def test_883_357_185_IsInvalid(self):
        self.assertFalse(self.validator.IsTriangleValid([883, 357, 185]))


class TriangleValidator:
    def __init__(self):
        pass

    def IsTriangleValid(self, sideLengths):
        for side1, side2, side3 in itertools.permutations(sideLengths, 3):
            if (side1 + side2) <= side3:
                return False
        return True

if __name__ == '__main__':
    validator = TriangleValidator()
    validTrianglePart1 = 0
    validTrianglePart2 = 0
    with open('input', 'r') as f:
        for line in f:
            sideLengths = map(int, line.strip('\n').split())
            if validator.IsTriangleValid(sideLengths):
                validTrianglePart1 += 1
    with open('input', 'r') as f:
        while True:
            next3Lines = list(itertools.islice(f, 3))
            if not next3Lines:
                break
            line1 = next3Lines[0].strip('\n').split()
            line2 = next3Lines[1].strip('\n').split()
            line3 = next3Lines[2].strip('\n').split()

            triangle1 = map(int, [line1[0], line2[0], line3[0]])
            triangle2 = map(int, [line1[1], line2[1], line3[1]])
            triangle3 = map(int, [line1[2], line2[2], line3[2]])

            for triangle in [triangle1, triangle2, triangle3]:
                print triangle
                if validator.IsTriangleValid(triangle):
                    validTrianglePart2 += 1

    print 'Part 1:', validTrianglePart1
    print 'Part 2:', validTrianglePart2
