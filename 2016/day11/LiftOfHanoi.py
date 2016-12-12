import copy
import itertools
import unittest


class LiftOfHanoi:
    def __init__(self):
        self.initialFloor = 1
        self.initialfloorContents = {1: ['TG', 'TM', 'PG', 'SG'],
                                     2: ['PM', 'SM'],
                                     3: ['OG', 'OM', 'RG', 'RM'],
                                     4: []}
        self.moves = list()
        self.states = set()

    def solve(self):
        goal = sum([len(floorItems) for floorItems in self.initialfloorContents.values()])
        possibleItems = [items for numberOfItems in range(1, 3) for items in itertools.combinations(self.initialfloorContents[self.initialFloor], numberOfItems)]
        self.moves = [(move, (copy.deepcopy(self.initialfloorContents), self.initialFloor), 1) for move in self.getPossibleMoves(possibleItems, [1])]

        while len(self.moves) > 0:
            move, state, iteration = self.moves.pop(0)
            objects = move[0]
            direction = move[1]
            floorContents = state[0]
            oldFloor = state[1]
            currentFloor = oldFloor + direction
            for object in objects:
                floorContents[oldFloor].remove(object)
                floorContents[currentFloor].append(object)
            if len(floorContents[4]) == goal:
                return iteration
            if (self.validArrangement(floorContents[currentFloor])) and (self.validArrangement(floorContents[oldFloor])):
                pairedContents = self.getPairs(floorContents)
                currentState = (pairedContents, currentFloor)
                if currentState not in self.states:
                    self.states.add(currentState)
                    itemCombinationsAvailableOnThisFloor = [items for numberOfItems in range(1, 3) for items in itertools.combinations(floorContents[currentFloor], numberOfItems)]
                    minFloor = 1
                    while len(floorContents[minFloor]) == 0:
                        minFloor += 1
                    if currentFloor == minFloor:
                        possibleDirections = [1]
                    elif currentFloor == 4:
                        possibleDirections = [-1]
                    else:
                        possibleDirections = [-1, 1]
                    newMovesFromCurrentState = [(move, (copy.deepcopy(floorContents), currentFloor), iteration + 1) for move in self.getPossibleMoves(itemCombinationsAvailableOnThisFloor, possibleDirections)]
                    for combo in newMovesFromCurrentState:
                        self.moves.append(combo)
        return -1

    def getPairs(self, floorContents):
        generators = [(floor, item[0]) for floor in range(1, 5) for item in floorContents[floor] if 'G' in item]
        chips = [(floor, item[0]) for floor in range(1, 5) for item in floorContents[floor] if 'M' in item]
        pairs = tuple([tuple(sorted([floorGen, floorChip])) for (floorGen, gen) in generators for (floorChip, chip) in chips if gen == chip])
        return pairs

    def getPossibleMoves(self, itemCombinationsAvailableOnThisFloor, possibleDirections):
        return [move for move in itertools.product(itemCombinationsAvailableOnThisFloor, possibleDirections)]

    def validArrangement(self, floor):
        if len(floor) == 0:
            return True
        generators = [item[0] for item in floor if item[1] == 'G']
        chips = [item[0] for item in floor if item[1] == 'M']
        if len(generators) == 0:
            return True
        if len(chips) == 0:
            return True
        for chip in chips:
            if (chip not in generators) and (len(generators) > 0):
                return False
        return True


class TestListOfHanoi(unittest.TestCase):
    def setUp(self):
        self.lift = LiftOfHanoi()

    def test_GetFloorsOfPairs(self):
        pairs = self.lift.getPairs({1: ['HM', 'LM'],
                                    2: ['HG'],
                                    3: ['LG'],
                                    4: []})
        self.assertEqual(tuple([(1, 2), (1, 3)]), pairs)

    def test_ValidCheck(self):
        self.assertTrue(self.lift.validArrangement(['HG', 'HM']))
        self.assertTrue(self.lift.validArrangement([]))
        self.assertTrue(self.lift.validArrangement(['LM', 'HM']))
        self.assertFalse(self.lift.validArrangement(['HG', 'HM', 'LM']))
        self.assertTrue(self.lift.validArrangement(['HG', 'LG', 'LM']))
        self.assertTrue(self.lift.validArrangement(['HG', 'HM', 'LM', 'LG']))

    def test_GetPossMoves(self):
        self.assertEqual([(('HG',), 1), (('HM',), 1), (('HG', 'HM'), 1)], self.lift.getPossibleMoves([('HG',), ('HM',), ('HG', 'HM')], [1]))

    def test_WithExampleInput(self):
        self.lift.initialfloorContents = {1: ['HM', 'LM'],
                                          2: ['HG'],
                                          3: ['LG'],
                                          4: []}
        self.assertEqual(11, self.lift.solve())

    def test_WithRealPart1Input(self):
        self.assertEqual(31, self.lift.solve())

    def test_WithRealPart2Input(self):
        self.lift.initialfloorContents[1].append('EG')
        self.lift.initialfloorContents[1].append('EM')
        self.lift.initialfloorContents[1].append('DG')
        self.lift.initialfloorContents[1].append('DM')
        self.assertEqual(55, self.lift.solve())

if __name__ == '__main__':
    lift = LiftOfHanoi()
    print 'Part 1:', lift.solve()
    liftPart2 = LiftOfHanoi()
    liftPart2.initialfloorContents[1].append('EG')
    liftPart2.initialfloorContents[1].append('EM')
    liftPart2.initialfloorContents[1].append('DG')
    liftPart2.initialfloorContents[1].append('DM')
    print 'Part 2:', liftPart2.solve()
