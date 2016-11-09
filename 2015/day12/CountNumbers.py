import json


def count(object):
    if type(object) in [str, unicode]:
        return 0
    if type(object) in [int, float]:
        return object
    if type(object) is dict:
        object = object.values()
    if type(object) is list:
        return sum(map(count, object))
    total = 0
    return total


def countPart2(object):
    if type(object) in [str, unicode]:
        return 0
    if type(object) in [int, float]:
        return object
    if type(object) is dict:
        if 'red' in object.keys() or 'red' in object.values():
            return 0
        object = object.values()
    if type(object) is list:
        return sum(map(countPart2, object))
    total = 0
    return total


def parseInput(filename):
    input = json.loads(open(filename, 'r').read())
    return count(input)


def parseInput2(filename):
    input = json.loads(open(filename, 'r').read())
    return countPart2(input)


if __name__ == '__main__':
    print parseInput('input.txt')
    print parseInput2('input.txt')
