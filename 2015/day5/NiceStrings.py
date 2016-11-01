from itertools import groupby


def IsNice(string):
    if CountVowels(string) < 3:
        return False
    if not IsAnyLetterFoundAdjacentToSameLetter(string):
        return False
    if StringContainsDisallowedCombinations(string):
        return False
    return True


def StringContainsDisallowedCombinations(string):
    if ('ab' in string) or ('cd' in string) or ('pq' in string) or ('xy' in string):
        return True
    return False


def IsAnyLetterFoundAdjacentToSameLetter(string):
    for (letter, count) in [[k, len(list(g))] for k, g in groupby(string)]:
        if count >= 2:
            return True
    return False


def CountVowels(string):
    vowels = 'aeiou'
    numberOfVowels = 0
    for vowel in vowels:
        numberOfVowels += string.count(vowel)
    return numberOfVowels


def PairIsRepeatedTwice(string):
    for i, letter in enumerate(string[:-1]):
        testSubString = letter + string[i + 1]
        if (testSubString in string[:i]) or (testSubString in string[i + 2:]):
            return True
    return False


def CharIsRepeatedWithSeperatingChar(string):
    for i, letter in enumerate(string[:-2]):
        if letter is string[i + 2]:
            return True
    return False


def IsNiceNewRules(string):
    if not PairIsRepeatedTwice(string):
        return False
    if not CharIsRepeatedWithSeperatingChar(string):
        return False
    return True

with open('input.txt', 'r') as f:
    newRulesCounter = 0
    oldRulesCounter = 0
    lines = []
    for line in f:
        if IsNice(line):
            oldRulesCounter += 1
        if IsNiceNewRules(line):
            newRulesCounter += 1
    print 'Part 1: ', oldRulesCounter, 'Part 2:', newRulesCounter
