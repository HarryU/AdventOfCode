import hashlib
import itertools
import unittest


class TestKeypadHash(unittest.TestCase):
    def setUp(self):
        pass

    def test_Contains3RepeatedChars(self):
        self.assertEqual('1', containsNCharsInARow('abcd111efghij', 3))

    def test_Contains5RepeatedChars(self):
        self.assertEqual('1', containsNCharsInARow('abcd11111efghij', 5))

    def test_DoesntHave3RepeatedChars(self):
        self.assertEqual(0, len(containsNCharsInARow('abcdefghij', 3)))

    def test_DoesntHave5RepeatedChars(self):
        self.assertEqual(0, len(containsNCharsInARow('abcde111fghij', 5)))

    def test_Has3AndOtherHasSame5(self):
        self.assertTrue(containsNCharsInARow('abcdaaaefghij', 3) == containsNCharsInARow('aaaaabcdefghij', 5))

    def test_Has3AndOtherDoesntHaveSame5(self):
        self.assertFalse(containsNCharsInARow('abcdaaaefghij', 3) == containsNCharsInARow('aabcdeaaafghij', 5))


def containsNCharsInARow(string, n):
    consecutiveRepeatedLetterCounts = [(letter, len(list(occurrences))) for letter, occurrences in itertools.groupby(string)]
    for letter, count in consecutiveRepeatedLetterCounts:
        if count >= n:
            return letter
    return []

def findNRepeatedOfChar(string, n, char):
    if str(char * 5) in string:
        return True
    return False


def hashString(string):
    return hashlib.md5(string).hexdigest()


def part2Hash(string):
    for _ in range(2017):
        string = hashString(string)
    return string


def solve(salt, hashFunction):

    keypad = []
    i = 0
    hashes = []
    for intToHash in range(1001):
        hash = hashFunction(salt + str(intToHash))
        hashes.append(hash)
    while len(keypad) < 64:
        hash = hashes.pop(0)
        charToMatch = containsNCharsInARow(hash, 3)
        if len(charToMatch) > 0:
            for hash in hashes:
                if findNRepeatedOfChar(hash, 5, charToMatch):
                    keypad.append(i)
        i += 1
        hashes.append(hashFunction(salt + str(i + len(hashes))))
    return keypad[-1]


if __name__ == '__main__':
    print 'Part 1 example (22728):', solve('abc', hashString)
    print 'Part 1 real (23890):', solve('ahsbgdzn', hashString)
    print 'Part 2 example (22551):', solve('abc', part2Hash)
    print 'Part 2 real ():', solve('ahsbgdzn', part2Hash)
