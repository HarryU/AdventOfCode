import unittest
import wrappingPaperCalculator

class WrappingPresentsTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_wrappingPaperCalulatorWithExampleInput(self):
        result = wrappingPaperCalculator.calculatePresentSize('2x3x4')
        self.assertEqual(58, result)

    def test_ribbonCalculator(self):
        result = wrappingPaperCalculator.calculateRibbonLength('2x3x4')
        self.assertEqual(34, result)


