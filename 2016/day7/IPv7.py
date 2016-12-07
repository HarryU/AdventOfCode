import unittest


def StringContainsAbba(string):
    i = 0
    while i + 3 < len(string):
        if (string[i:i+2] == string[i+2:i+4][::-1]) and (string[i] != string[i+1]):
            return True
        i += 1
    return False


def StringContainsAba(string):
    i = 0
    abaStrs = []
    while i + 2 < len(string):
        if string[i] != string[i+1] and (string[i] == string[i+2]):
            abaStrs.append(string[i:i+3])
        i += 1
    if len(abaStrs) > 0:
        return abaStrs
    return False


def SplitStringAtSqrBrackets(string):
    outsideSqrBrackets = []
    insideSqrBrackets = []
    splitStr = string.split('[')
    for subStr in splitStr:
        if ']' in subStr:
            newSubStrs = subStr.split(']')
            insideSqrBrackets.append(newSubStrs[0])
            outsideSqrBrackets.append(newSubStrs[1])
        else:
            outsideSqrBrackets.append(subStr)
    return outsideSqrBrackets, insideSqrBrackets


def StringTesterPart1(string):
    outsideStrings, insideStrings = SplitStringAtSqrBrackets(string)
    if any([StringContainsAbba(string) for string in outsideStrings]) and not any([StringContainsAbba(string) for string in insideStrings]):
        return True


def StringTesterPart2(string):
    outsideStrings, insideStrings = SplitStringAtSqrBrackets(string)
    abaStrings = [StringContainsAba(subStr) for subStr in outsideStrings]
    for abas in abaStrings:
        if abas:
            for aba in abas:
                assert aba is not False
                bab = ''.join([aba[1], aba[0], aba[1]])
                for subStr in insideStrings:
                    if bab in subStr:
                        return True
    return False


class TestAbbaStringCounter(unittest.TestCase):
    def test_ABBAReturnsTrue(self):
        self.assertTrue(StringContainsAbba('abba'))

    def test_BABAReturnsFalse(self):
        self.assertFalse(StringContainsAbba('baba'))

    def test_StringSplitWorks(self):
        testString = 'abcde[fghij]klmno[pqrst]uvw'
        insideStrings = ['fghij', 'pqrst']
        outsideStrings = ['abcde', 'klmno', 'uvw']
        resultOut, resultIn = SplitStringAtSqrBrackets(testString)
        self.assertEqual(insideStrings, resultIn)
        self.assertEqual(outsideStrings, resultOut)

    def test_StringTesterWithValidString(self):
        self.assertTrue(StringTesterPart1('abba[mnop]qrst'))

    def test_StringTesterWithInvalidString(self):
        self.assertFalse(StringTesterPart1('abba[mnnm]qrst'))

    def test_StringTesterWithLongInvalidString(self):
        self.assertFalse(StringTesterPart1('abbaaaaabbsb[neenmnyet]jklmnop[baanmmn]yyyylkkl'))

    def test_StringWithSamePairRepeated(self):
        self.assertFalse(StringTesterPart1('aaaa[bcde]fghi'))

    def test_StringContainsABA(self):
        self.assertTrue(StringContainsAba('ccccabacccc'))

    def test_StringDoesntContainABA(self):
        self.assertFalse(StringContainsAba('aaabbbccc'))

    def test_StringTesterPart2(self):
        self.assertTrue(StringTesterPart2('aba[bab]cde'))
        self.assertTrue(StringTesterPart2('aaa[kek]eke'))
        self.assertTrue(StringTesterPart2('aba[bab]xyz'))
        self.assertTrue(StringTesterPart2('zazbz[bzb]cdb'))

    def test_StringTesterPart2WithInvalid(self):
        self.assertFalse(StringTesterPart2('xyx[xyx]xyx'))

if __name__ == '__main__':
    with open('input', 'r') as f:
        validP1 = 0
        validP2 = 0
        for line in f:
            if StringTesterPart1(line.strip('\n')):
                validP1 += 1
            if StringTesterPart2(line.strip('\n')):
                validP2 += 1
        print 'Part 1:', validP1
        print 'Part 2:', validP2
