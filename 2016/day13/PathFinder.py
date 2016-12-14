import copy
import cv2
import numpy as np
import unittest


class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = Map(50, 50)

    def test_SolveExample(self):
        self.assertEqual(11, self.map.solve(targetLocation=(7, 4), puzzleInput=10)[0])

    def test_SolvePart1(self):
        realMap = Map()
        self.assertEqual(86, realMap.solve(targetLocation=(31, 39), puzzleInput=1364)[0])
        self.assertEqual(127, realMap.solve(targetLocation=(31, 39), puzzleInput=1364, part2=True)[0])

    def test_PossibleMoves(self):
        self.assertEqual({(1, 0), (0, 1)}, self.map.possibleMoves((0, 0)))


class Map:
    def __init__(self, m=100, n=100):
        self.map = np.zeros((m, n, 3))

    def fillMap(self, puzzleInput=1364):
        '''
        Fill the map with walls and spaces for display purposes.
        '''
        for x in range(self.map.shape[0]):
            for y in range(self.map.shape[1]):
                if self.wallOrSpace(x, y, puzzleInput) == 0:
                    self.map[y, x] = (255, 255, 255)

    def wallOrSpace(self, x, y, puzzleInput=1364):
        '''
        Returns 1 if the position represents a wall and 0 if it represents open space.
        :param x: x co-ordinate of the position.
        :param y: y co-ordinate of the position.
        :param puzzleInput: defaults to my puzzle input (1364). Can be any integer.
        :return: 0 if not a wall, 1 if a wall
        '''
        equation = (x ** 2) + (3 * x) + (2 * x * y) + y + (y ** 2) + puzzleInput
        ones = bin(equation).count('1')
        if ones % 2 == 0:
            return 0
        else:
            return 1

    def possibleMoves(self, location):
        '''
        Returns a set of the possible single step moves that don't move to a position below 0 in x or y.
        :param location: Tuple in the format (x, y)
        :return: Set of tuples that represent possible moves. xDir and yDir can either be 0, 1 or -1. {(xDir, yDir), (xDir, yDir)}
        '''
        x, y = location
        return {(xDir, yDir) for xDir in (0, 1, -1) for yDir in (0, 1, -1) if ((abs(xDir) + abs(yDir)) == 1) and ((xDir + x) >= 0) and ((yDir + y) >= 0)}

    def solve(self, initialLocation=(1, 1), targetLocation=(31, 39), puzzleInput=1364, part2=False):
        '''
        Find the shortest path from initialLocation to targetLocation.
        :param initialLocation: start point for state (defaults to (1, 1))
        :param targetLocation: target endpoint (defaults to 31, 39)
        :param puzzleInput: defaults to my puzzle input (1364). Can be any integer.
        :return: iterations in shortest path,
                    possible unique visitable nodes in up to 50 moves,
                    shortest path to target location
        '''
        seenCoordinates = [initialLocation]
        initialTargetDistance = self.aStarCost(initialLocation, 0, targetLocation)
        moves = [([(move, seenCoordinates)], initialLocation, initialTargetDistance, 1) for move in self.possibleMoves(initialLocation)]
        numberOfMoves = 0
        part1 = 0
        bestPath = []
        self.map[targetLocation[1], targetLocation[0]] = (255, 0, 0)
        self.map[initialLocation[1], initialLocation[0]] = (0, 0, 255)
        while len(moves) > 0:
            if not part2:
                moves = sorted(moves, key=lambda moveInformation: moveInformation[2])
            currentPath, oldLocation, distance, currentIteration = moves.pop(0)
            if part2:
                if currentIteration > 50:
                    return len(seenCoordinates), []
            currentMove = currentPath[-1][0]
            currentLocation = (currentMove[0] + oldLocation[0], currentMove[1] + oldLocation[1])
            if currentLocation == targetLocation:
                part1 = currentIteration
                bestPath = list(currentPath)
                return part1, bestPath

            if (currentLocation[0] >= 0) and (currentLocation[1] >= 0):
                if currentLocation not in seenCoordinates:
                    if self.wallOrSpace(currentLocation[0], currentLocation[1], puzzleInput) == 0:
                        costOfNode = self.aStarCost(currentLocation, len(currentPath), targetLocation)
                        print seenCoordinates
                        seenCoordinates.append(currentLocation)
                        numberOfMoves += 1
                        for move in self.possibleMoves(currentLocation):
                            newPath = list(currentPath)
                            currentState = copy.deepcopy(seenCoordinates)
                            newPath.append((move, currentState))
                            moves.append((newPath, currentLocation, costOfNode, currentIteration + 1))
        return part1, bestPath

    def aStarCost(self, currentLocation, g, targetLocation):
        '''
        A cost function for optimising a BFS into an A* search.
        :param currentLocation: Current position in the map.
        :param g: Length of path currently being considered.
        :param targetLocation: Target position.
        :return: f(n) = g(n) + h(n), where g(n) is the cost of reaching node n, and h(n) is the estimated cost to reach the target.
        '''
        h = (abs(targetLocation[0] - currentLocation[0])**2 + abs(targetLocation[1] - currentLocation[1])**2)**0.5
        return h + g


if __name__ == '__main__':
    map = Map()
    initiaLocation = (1, 1)
    map.fillMap()
    path = map.solve()[1]
    x, y = initiaLocation
    for move, state in path[:-1]:
        for pixel in state:
            map.map[pixel[1], pixel[0]] = (0.4, 0.4, 0.4)
        x += move[0]
        y += move[1]
        map.map[y, x] = (0, 1, 0)
        cv2.imshow('Map', cv2.resize(map.map, None, fx=10, fy=10, interpolation=cv2.INTER_AREA))
        cv2.waitKey(100)
    cv2.imshow('Map', cv2.resize(map.map, None, fx=10, fy=10, interpolation=cv2.INTER_AREA))
    cv2.waitKey(0)
