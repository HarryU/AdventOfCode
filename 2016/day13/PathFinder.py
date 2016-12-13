import cv2
import numpy as np
import unittest


class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = Map(7, 10)

    def test_SolveExample(self):
        self.assertEqual(11, self.map.solve(targetLocation=(7, 4), puzzleInput=10))

    def test_SolvePart1(self):
        realMap = Map()
        self.assertEqual((86, 127), realMap.solve(targetLocation=(31, 39), puzzleInput=1364))


class Map:
    def __init__(self, m=100, n=100):
        self.map = np.zeros((m, n))

    def fillMap(self, puzzleInput=1364):
        for y in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                self.map[y, x] = self.wallOrSpace(puzzleInput, x, y)

    def wallOrSpace(self, x, y, puzzleInput=1364):
        equation = (x ** 2) + (3 * x) + (2 * x * y) + y + (y ** 2) + puzzleInput
        binary = format(equation, 'b')
        ones = sum([1 for digit in binary if digit == '1'])
        if ones % 2 == 0:
            return 0
        else:
            return 1

    def possibleMoves(self, location):
        if (location[0] != 0) and (location[1] != 0):
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif location[0] != 0:
            return [(1, 0), (0, -1), (0, 1)]
        elif location[1] != 0:
            return [(-1, 0), (1, 0), (0, 1)]
        else:
            return [(1, 0), (0, 1)]

    def solve(self, initialLocation=(1, 1), targetLocation=(31, 39), puzzleInput=1364):
        seenCoordinates = {initialLocation}
        currentLocation = initialLocation
        moves = [((-1, 0), currentLocation, 1),
                 ((1, 0), currentLocation, 1),
                 ((0, -1), currentLocation, 1),
                 ((0, 1), currentLocation, 1)]
        numberOfMoves = 0
        part2 = 0
        while len(moves) > 0:
            currentMove, oldLocation, currentIteration = moves.pop(0)
            currentLocation = (currentMove[0] + oldLocation[0], currentMove[1] + oldLocation[1])
            print currentLocation, currentIteration
            if currentLocation == targetLocation:
                return currentIteration, part2
            if currentLocation not in seenCoordinates:
                seenCoordinates.add(currentLocation)
                if self.wallOrSpace(currentLocation[0], currentLocation[1], puzzleInput) == 0:
                    numberOfMoves += 1
                    for move in self.possibleMoves(currentLocation):
                        moves.append((move, currentLocation, currentIteration + 1))
            if currentIteration == 50:
                part2 = numberOfMoves
        return -1, part2

if __name__ == '__main__':
    map = Map()
    map.fillMap()
    cv2.imshow('Map', cv2.resize(map.map, None, fx=10, fy=10))
    cv2.waitKey(0)