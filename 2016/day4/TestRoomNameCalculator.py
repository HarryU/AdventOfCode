from collections import Counter
import unittest


class TestRoomNameChecker(unittest.TestCase):
    def setUp(self):
        self.checker = RoomNameChecker()
        self.testRoomStrings = ['aaaaa-bbb-z-y-x-123[abxyz]',
                                'a-b-c-d-e-f-g-h-987[abcde]',
                                'not-a-real-room-404[oarel]',
                                'totally-real-room-200[decoy]']

    def test_stringParsing(self):
        name, sectorID, checksum = self.checker.parseNewRoomName('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertEqual('aaaaabbbzyx', ''.join(name))
        self.assertEqual(123, sectorID)
        self.assertEqual('abxyz', checksum)

    def test_NameIsValid(self):
        name, sectorID, checksum = self.checker.parseNewRoomName('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertTrue(self.checker.validName(name, checksum))

    def test_NameIsNotValid(self):
        name, sectorID, checksum = self.checker.parseNewRoomName('totally-real-room-200[decoy]')
        self.assertFalse(self.checker.validName(name, checksum))

    def test_OtherValidName(self):
        name, sectorID, checksum = self.checker.parseNewRoomName('not-a-real-room-404[oarel]')
        self.assertTrue(self.checker.validName(name, checksum))

    def test_ShiftChar(self):
        self.assertEqual('b', self.checker.getNewChar(ord('a'), 1))

    def test_DecryptName(self):
        testName = 'qzmt-zixmtkozy-ivhz-343[junkval]'
        name, sectorID, chceksum = self.checker.parseNewRoomName(testName)
        self.assertEqual('veryencryptedname', self.checker.decryptName(name, sectorID))

    def test_SumValidRooms(self):
        for string in self.testRoomStrings:
            self.checker.addRoom(string)
        self.assertEqual(1514, self.checker.totalSectorID)


class RoomNameChecker:
    def __init__(self):
        self.totalSectorID = 0

    def addRoom(self, string):
        name, sectorID, checksum = self.parseNewRoomName(string)
        if self.validName(name, checksum):
            self.totalSectorID += sectorID
            realName = self.decryptName(name, sectorID)
            print realName
            if 'north' in realName:
                print 'Part 2:', sectorID

    def decryptName(self, name, id):
        decrypted = ''
        decryptionTable = {}
        for char in ''.join(set(''.join(name))):
            newChar = self.getNewChar(ord(char), id)
            decryptionTable[char] = newChar
        for char in ''.join(name):
            decrypted += decryptionTable[char]
        return ''.join(decrypted)

    def getNewChar(self, charOrd, id):
        id %= 26
        newCharOrd = charOrd + id
        while newCharOrd not in range(ord('a'), ord('z') + 1):
            if newCharOrd > ord('z'):
                newCharOrd -= 26
            elif newCharOrd < ord('a'):
                newCharOrd += 26
        return chr(newCharOrd)

    def parseNewRoomName(self, rawName):
        name = rawName.strip('\n').split('-')
        checksumAndID = name[-1].strip(']').split('[')
        name = name[:-1]
        sectorID = checksumAndID[0]
        checksum = checksumAndID[1]
        return name, int(sectorID), checksum

    def validName(self, name, checksum):
        letters = dict(Counter(''.join(name))).items()
        letters.sort(key=lambda x: x[0])
        letters.sort(key=lambda x: x[1], reverse=True)
        correctChecksum = ''.join([letter for letter, count in letters])[:5]
        if checksum == correctChecksum:
            return True
        return False

if __name__ == '__main__':
    checker = RoomNameChecker()
    with open('input', 'r') as f:
        for line in f:
            checker.addRoom(line)
    print 'Part 1:', checker.totalSectorID
