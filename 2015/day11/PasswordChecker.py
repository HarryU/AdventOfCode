from itertools import groupby
import string
# import unittest
#
#
# class TestPasswordChecker(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def test_ExampleFailsRuleOne(self):
#         self.assertFalse(RuleOne('abbceffg'))
#
#     def test_ExamplePassesRuleOne(self):
#         self.assertTrue(RuleOne('hijklmn'))
#
#     def test_ExamplePassesRuleTwo(self):
#         self.assertTrue(RuleTwo('abbceffg'))
#
#     def test_ExampleFailsRuleTwo(self):
#         self.assertFalse(RuleTwo('hijklmn'))
#
#     def test_ExamplePassesRuleThree(self):
#         self.assertTrue(RuleThree('abbcegjj'))
#
#     def test_ExampleFailsRuleThree(self):
#         self.assertFalse(RuleThree('abbcegjk'))
#
#     def test_IncrementPassword(self):
#         self.assertEqual('kdyehdnj', IncrementPassword('kdyehdni'))


def IncrementPassword(password):
    i = 0
    r = list(password)[::-1]
    for c in r:
        if c == 'z':
            r[i] = 'a'
        else:
            r[i] = chr(ord(c) + 1)
            break
        i += 1
    password = ''.join(r[::-1])
    return password


def ValidPassword(string):
    if not RuleOne(string):
        return False
    if not RuleTwo(string):
        return False
    if not RuleThree(string):
        return False
    return True


def RuleOne(string):
    for i in range(len(string) - 2):
        if (charInDec(string[i]) == charInDec(string[i+1]) - 1) and (charInDec(string[i]) == charInDec(string[i+2]) - 2):
            return True
    return False


def RuleTwo(string):
    if ('i' in string) or ('o' in string) or ('l' in string):
        return False
    return True


def RuleThree(string):
    moreThan2 = 0
    for (letter, count) in [[k, len(list(g))] for k, g in groupby(string)]:
        if count >= 2:
            moreThan2 += 1
        if moreThan2 >= 2:
            return True
    return False


def charInDec(char):
    return int(string.ascii_lowercase.index(char))

if __name__ == '__main__':
    password = 'cqjxjnds'
    while not ValidPassword(password):
        password = IncrementPassword(password)
    print password
    password = IncrementPassword(password)
    while not ValidPassword(password):
        password = IncrementPassword(password)
    print password