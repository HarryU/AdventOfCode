def charsOfCode(s):
    return len(s)


def charsInString(s):
    count = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == "\\":
            i += 4 if s[i + 1] == "x" else 2
        else:
            i += 1
        count += 1
    return count


def encodedLength(s):
    return len(s) + s.count('\\') + s.count('"') + 2


if __name__ == '__main__':
    code = 0
    string = 0
    encoded = 0
    extraChars = 0
    with open('input.txt', 'r') as inputFile:
        for line in inputFile:
            code += charsOfCode(line)
            string += charsInString(line)
            encoded += encodedLength(line)
    print "Part 1: ", code - string
    print "Part 2: ", encoded - code
