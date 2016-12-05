import NiceStrings
import unittest


class NiceStringsTests(unittest.TestCase):
    def setUp(self):
        self.testString = 'ugknbfddgicrmopn'

    def test_ExampleStringIsNice(self):
        self.assertTrue(NiceStrings.IsNice(self.testString))

    def test_SecondExampleString(self):
        self.assertTrue(NiceStrings.IsNiceNewRules('abcbc'))
        self.assertTrue(NiceStrings.IsNiceNewRules('xxyxx'))
        self.assertFalse(NiceStrings.IsNiceNewRules('abcd'))
        self.assertFalse(NiceStrings.IsNiceNewRules('abcdefaaahijklmno'))

    def test_AdjacentLetters(self):
        self.assertTrue(NiceStrings.IsAnyLetterFoundAdjacentToSameLetter(self.testString))

    def test_DisallowedStrings(self):
        self.assertFalse(NiceStrings.StringContainsDisallowedCombinations(self.testString))

    def test_VowelCounterWith3Vowels(self):
        numberOfVowels = NiceStrings.CountVowels(self.testString)
        self.assertEqual(3, numberOfVowels)

    def test_PairOfCharsIsRepeated(self):
        self.assertTrue(NiceStrings.PairIsRepeatedTwice('aabcdefgaa'))
        self.assertFalse(NiceStrings.PairIsRepeatedTwice('mmggfwapsetemiuj'))

    def test_CharIsRepeatedWithOneCharSeparating(self):
        self.assertTrue(NiceStrings.CharIsRepeatedWithSeperatingChar('xyx'))
        self.assertTrue(NiceStrings.CharIsRepeatedWithSeperatingChar('aaa'))
        self.assertFalse(NiceStrings.CharIsRepeatedWithSeperatingChar('abc'))
