import SueSelector
import unittest

class TestSueSelector(unittest.TestCase):
    def setUp(self):
        self.filename = 'input.txt'

    def test_ParsingFile(self):
        sues = SueSelector.AllSues(self.filename)
        self.assertEqual(9, sues.sues[1]['cars'])
        self.assertEqual(3, sues.sues[1]['akitas'])
        self.assertEqual(0, sues.sues[1]['goldfish'])
