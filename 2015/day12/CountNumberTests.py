import CountNumbers
import unittest


class TestCountNumbers(unittest.TestCase):
    def setUp(self):
        pass

    def test_ParsingFile(self):
        self.assertEqual(6, CountNumbers.parseInput('testInput_6.txt'))

    def test_Part2Counting(self):
        self.assertEqual(4, CountNumbers.parseInput2('testInput2_4.txt'))