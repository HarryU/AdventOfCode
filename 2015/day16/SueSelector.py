class AllSues:
    def __init__(self, filename):
        self.sues = dict()
        self.ParseFile(filename)

    def ParseFile(self, filename):
        with open(filename, 'r') as inputFile:
            for line in inputFile:
                line = line.strip('\n')
                sueNumber = int(line.split(':')[0].split(' ')[1])
                categoryNames = list()
                categoryValues = list()
                for string in ''.join(line.split(':')[1:]).split(','):
                    categoryNames.append(string.split(' ')[1:][0])
                    categoryValues.append(int(string.split(' ')[1:][1]))
                self.sues[sueNumber] = dict(zip(categoryNames, categoryValues))

    def CompareSue(self, testSue):
        for sue in self.sues.keys():
            validSue = True
            for category in testSue.keys():
                if category in self.sues[sue]:
                    if self.sues[sue][category] != testSue[category]:
                        validSue = False
                        break
            if validSue:
                return sue

if __name__ == '__main__':
    sues = AllSues('input.txt')
    sueDict = {'children': 3,
               'cats': 7,
               'samoyeds': 2,
               'pomeranians': 3,
               'akitas': 0,
               'vizslas': 0,
               'goldfish': 5,
               'trees': 3,
               'cars': 2,
               'perfumes': 1
               }
    print sues.CompareSue(sueDict)
