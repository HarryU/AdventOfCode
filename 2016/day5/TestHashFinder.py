import hashlib
import unittest


class TestHashFinder(unittest.TestCase):
    def setUp(self):
        self.finder = HashFinder('abc')

    def test_WithTestInput(self):
        self.assertEqual('18f47a30', self.finder.passwordPart1)

    def test_WithTestInputPart2(self):
        self.assertEqual('05ace8e3', self.finder.passwordPart2)


class HashFinder:
    def __init__(self, doorID):
        self.doorID = doorID
        self.index = 0
        self.passwordPart1 = ''
        self.passwordPart2 = [None] * 8
        self.charsUpTo8 = map(str, range(8))
        self.findPasswords()

    def findPasswords(self):
        while (len(self.passwordPart1) < 8) or (None in self.passwordPart2):
            m = hashlib.md5()
            m.update(self.doorID + str(self.index))
            hexMD5 = m.hexdigest()
            if hexMD5[:5] == '00000':
                if len(self.passwordPart1) < 8:
                    self.passwordPart1 += hexMD5[5]
                if hexMD5[5] in self.charsUpTo8:
                    if self.passwordPart2[int(hexMD5[5])] is None:
                        self.passwordPart2[int(hexMD5[5])] = hexMD5[6]
            self.index += 1
        self.passwordPart2 = ''.join(self.passwordPart2)

if __name__ == '__main__':
    finder = HashFinder('abbhdwsy')
    print 'Part 1: ', finder.passwordPart1
    print 'Part 2: ', finder.passwordPart2
