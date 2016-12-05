from collections import Counter
import itertools
import unittest


class TestEggnogStorage(unittest.TestCase):
    def setUp(self):
        self.storage = EggnogStorage([20, 15, 10, 5, 5], 25)

    def test_CheckCombination(self):
        self.assertTrue(self.storage.checkCombination([15, 10]))

    def test_CheckCombinationWithIncorrectCombination(self):
        self.assertFalse(self.storage.checkCombination([20, 10]))

    def test_GenerationOfAllCombinations(self):
        allCombinations = map(list, [(20,), (15,), (10,), (5,), (5,),
                           (20, 15), (20, 10), (20, 5), (20, 5), (15, 10), (15, 5), (15, 5), (10, 5), (10, 5), (5, 5),
                           (20, 15, 10), (20, 15, 5), (20, 15, 5), (20, 10, 5), (20, 10, 5), (20, 5, 5), (15, 10, 5),
                           (15, 10, 5), (15, 5, 5), (10, 5, 5),
                           (20, 15, 10, 5), (20, 15, 10, 5), (20, 15, 5, 5), (20, 10, 5, 5), (15, 10, 5, 5), (20, 15, 10, 5, 5)])
        self.assertEqual(allCombinations, self.storage.generateContainerCombinations())

    def test_CountValidCombinations(self):
        self.assertEqual(4, self.storage.countValidCombinations())


class EggnogStorage:
    def __init__(self, containers, volumeToStore=150):
        self.containers = containers
        self.volumeToStore = volumeToStore
        self.validCombinations = list()

    def checkCombination(self, combinationOfContainers):
        containerTotal = sum(combinationOfContainers)
        if containerTotal == self.volumeToStore:
            return True
        return False

    def generateContainerCombinations(self):
        combinations = []
        for i in range(1, len(self.containers) + 1):
            for combination in itertools.combinations(self.containers, i):
                combinations.append(list(combination))
        return combinations

    def countValidCombinations(self):
        for combination in self.generateContainerCombinations():
            if self.checkCombination(combination):
                self.validCombinations.append(combination)
        return len(self.validCombinations)

    def countValidCombinationsWithMinimumNumberOfContainers(self):
        lengths = [len(combo) for combo in self.validCombinations]
        minLength = min(lengths)
        counts = Counter(lengths)
        return counts[minLength]


if __name__ == '__main__':
    containers = []
    with open('input', 'r') as f:
        for container in f:
            containers.append(int(container))
    storage = EggnogStorage(containers)
    answer = storage.countValidCombinations()
    print 'Part 1: ', str(answer)
    print 'Part 2: ', str(storage.countValidCombinationsWithMinimumNumberOfContainers())

