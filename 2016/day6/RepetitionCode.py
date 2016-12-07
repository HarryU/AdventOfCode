from collections import Counter


def MostCommonLetters(strings):
    result = ''
    letters = ParseLettersByColumn(strings)
    for letterList in letters:
        occurrences = Counter(letterList)
        result += occurrences.most_common(1)[0][0]
    return result


def LeastCommonLetters(strings):
    result = ''
    letters = ParseLettersByColumn(strings)
    for letterList in letters:
        occurrences = Counter(letterList)
        result += occurrences.most_common()[::-1][0][0]
    return result


def ParseLettersByColumn(strings):
    letters = [[], [], [], [], [], [], [], []]
    for string in strings:
        string = string.strip('\n')
        for i, letter in enumerate(string):
            letters[i].append(letter)
    return letters

with open('input', 'r') as f:
    print 'Part 1: ', MostCommonLetters(f)
with open('input', 'r') as f:
    print 'Part 2: ', LeastCommonLetters(f)
