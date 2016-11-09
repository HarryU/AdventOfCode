import itertools

class SeatPlan:
    def __init__(self, filename):
        self.happinessValues = self.Parse(filename)

    def Parse(self, filename):
        valueDict = dict()
        with open(filename, 'r') as input:
            for line in input:
                lineSplit = line.strip('.\n').split(' ')
                person1 = lineSplit[0]
                if not person1 in valueDict.keys():
                    valueDict[person1] = dict()
                change = int(lineSplit[3])
                if 'lose' in lineSplit:
                    change *= -1
                person2 = lineSplit[-1]
                valueDict[person1][person2] = change
        return valueDict

    def GetHappinessChange(self, name1, name2):
        return int(self.happinessValues[name1][name2])

    def TotalHappiness(self, seatingOrder):
        total = 0
        for i in range(len(seatingOrder)):
            total += self.GetHappinessChange(seatingOrder[i], seatingOrder[i-1])
            total += self.GetHappinessChange(seatingOrder[i], seatingOrder[i+1 if i+1 < len(seatingOrder) else 0])
        return total

    def AddExtraPerson(self, name):
        self.happinessValues[name] = {}
        for person in self.happinessValues.keys():
            self.happinessValues[name][person] = 0
            self.happinessValues[person][name] = 0

    def GetAllSeatingOrders(self):
        return itertools.permutations(self.happinessValues.keys(), len(self.happinessValues.keys()))

if __name__ == '__main__':
    seating = SeatPlan('input.txt')
    happinessValues = list()
    for order in seating.GetAllSeatingOrders():
        happinessValues.append(seating.TotalHappiness(order))
    print 'Part 1: ', max(happinessValues)
    happinessValues2 = list()
    seatingPart2 = SeatPlan('input.txt')
    seatingPart2.AddExtraPerson('X')
    for order in seatingPart2.GetAllSeatingOrders():
        happinessValues2.append(seatingPart2.TotalHappiness(order))
    print 'Part 2:', max(happinessValues2)
