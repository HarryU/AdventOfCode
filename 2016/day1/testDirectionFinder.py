import unittest


class TestDirectionFinding(unittest.TestCase):
    def setUp(self):
        pass

    def test_StartDirectionIsNorth(self):
        directions = DirectionFind()
        dir = directions.getCurrentDirection()
        self.assertEqual('N', dir)

    def test_DirectionIsEastAfterRightTurn(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        dir = directions.getCurrentDirection()
        self.assertEqual('E', dir)

    def test_DirectionIsWestAfterLeftTurn(self):
        directions = DirectionFind()
        directions.changeDirection('L')
        dir = directions.getCurrentDirection()
        self.assertEqual('W', dir)

    def test_DirectionIsNorthAfterRightThenLeft(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        directions.changeDirection('L')
        dir = directions.getCurrentDirection()
        self.assertEqual('N', dir)

    def test_DirectionIsWestAfter5LeftTurns(self):
        directions = DirectionFind()
        directions.changeDirection('L')
        directions.changeDirection('L')
        directions.changeDirection('L')
        directions.changeDirection('L')
        directions.changeDirection('L')
        dir = directions.getCurrentDirection()
        self.assertEqual('W', dir)

    def test_DistanceIs5BlocksAfterR2L3(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        directions.walkDistance(2)
        directions.changeDirection('L')
        directions.walkDistance(3)
        dist = directions.getDistanceFromStart()
        self.assertEqual(5, dist)

    def test_DistanceIs2AfterR2R2R2(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        directions.walkDistance(2)
        directions.changeDirection('R')
        directions.walkDistance(2)
        directions.changeDirection('R')
        directions.walkDistance(2)
        dist = directions.getDistanceFromStart()
        self.assertEqual(2, dist)

    def test_DistanceIs12AfterR5L5R5R3(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        directions.walkDistance(5)
        directions.changeDirection('L')
        directions.walkDistance(5)
        directions.changeDirection('R')
        directions.walkDistance(5)
        directions.changeDirection('R')
        directions.walkDistance(3)
        dist = directions.getDistanceFromStart()
        self.assertEqual(12, dist)

    def test_PositionIs44AfterR8R4R4R8(self):
        directions = DirectionFind()
        directions.changeDirection('R')
        directions.walkDistance(8)
        directions.changeDirection('R')
        directions.walkDistance(4)
        directions.changeDirection('R')
        directions.walkDistance(4)
        directions.changeDirection('R')
        directions.walkDistance(8)
        pos = directions.getPosition()
        self.assertEqual((4, 4), pos)

    def test_PositionIsMinus22AfterL2R2(self):
        directions = DirectionFind()
        directions.changeDirection('L')
        directions.walkDistance(2)
        directions.changeDirection('R')
        directions.walkDistance(2)
        pos = directions.getPosition()
        self.assertEqual((2, -2), pos)


class DirectionFind:
    def __init__(self):
        self.directions = ['N', 'E', 'S', 'W']
        self.currentDirection = 0
        self.NSDist = 0
        self.EWDist = 0

    def getCurrentDirection(self):
        return self.directions[self.currentDirection]

    def changeDirection(self, turnDirection):
        if turnDirection == 'L':
            self.currentDirection -= 1
            if self.currentDirection < 0:
                self.currentDirection += 4
        if turnDirection == 'R':
            self.currentDirection += 1
            if self.currentDirection > 3:
                self.currentDirection -= 4

    def walkDistance(self, distance):
        if self.directions[self.currentDirection] == 'N':
            self.NSDist += distance
        if self.directions[self.currentDirection] == 'S':
            self.NSDist -= distance
        if self.directions[self.currentDirection] == 'E':
            self.EWDist += distance
        if self.directions[self.currentDirection] == 'W':
            self.EWDist -= distance

    def getDistanceFromStart(self):
        return abs(self.NSDist) + abs(self.EWDist)

    def getPosition(self):
        return self.NSDist, self.EWDist


if __name__ == '__main__':
    directions = DirectionFind()
    positions = []
    solved = False
    with open('input', 'r') as f:
        instructions = f.read().split(',')
        for instruction in instructions:
            instruction = instruction.strip(' \n')
            directions.changeDirection(instruction[0])
            for _ in range(int(instruction[1:])):
                directions.walkDistance(1)
                if not solved:
                    position = directions.getPosition()
                    for pos in positions:
                        if pos == position:
                            solved = True
                            print 'Part 2:', directions.getDistanceFromStart()
                    positions.append(position)

    print 'Part 1: ', directions.getDistanceFromStart()
