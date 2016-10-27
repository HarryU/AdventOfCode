def calculatePresentSize(line):
    dims = getDimsAsInts(line)
    l, w, h = dims
    present = 2 * ((l * w) + (w * h) + (h * l))
    present += sorted(dims)[0] * sorted(dims)[1]
    return present


def getDimsAsInts(line):
    dims = line.strip('\n').split('x')
    dims = map(int, dims)
    return dims


def calculateRibbonLength(line):
    dims = sorted(getDimsAsInts(line))
    ribbon = (2 * dims[0]) + (2 * dims[1])
    ribbon += (dims[0] * dims [1] * dims[2])
    return ribbon


if __name__ == '__main__':
    def getPuzzleResult():
        with open('input.txt', 'r') as f:
            totalPaper = 0
            totalRibbon = 0
            for line in f:
                totalPaper += calculatePresentSize(line)
                totalRibbon += calculateRibbonLength(line)
        print 'Wrapping paper needed: ', totalPaper, '\n Ribbon needed: ', totalRibbon

    getPuzzleResult()