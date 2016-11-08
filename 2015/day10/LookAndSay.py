import itertools


def translate(number):
    return ''.join(str(len([1 for _ in v])) + k for k, v in itertools.groupby(number))
    # newNumber = []
    # for c, l in itertools.groupby(number):
    #     newNumber.append(str(len(list(l))))
    #     newNumber.append(c)
    # return "".join(newNumber)

if __name__ == '__main__':
    number = '1321131112'
    for i in range(40):
        print i
        number = translate(number)
    print 'Part 1: ', len(number)
    number = '1321131112'
    for i in range(50):
        print i
        number = translate(number)
    print 'Part 2: ', len(number)
