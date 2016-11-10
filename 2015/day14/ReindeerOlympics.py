import math
import operator


class ReindeerRace:
    def __init__(self, filename):
        self.allReindeer = list()
        self.ParseFile(filename)

    def GetPositions(self, time):
        racePositions = dict()
        for reindeer in self.allReindeer:
            racePositions[reindeer.name] = reindeer.GetPosition(time)
        return racePositions

    def GetPoints(self, time):
        points = dict()
        for reindeer in self.allReindeer:
            points[reindeer.name] = 0
        for seconds in range(time):
            positions = self.GetPositions(seconds + 1)
            leadingDistance = max(positions.iteritems(), key=operator.itemgetter(1))[1]
            for reindeer in positions.keys():
                if positions[reindeer] == leadingDistance:
                    points[reindeer] += 1
        return points

    def AddReindeer(self, name, speed, flyTime, restTime):
        self.allReindeer.append(Reindeer(name, speed, flyTime, restTime))

    def ParseFile(self, filename):
        with open(filename, 'r') as input:
            for line in input:
                words = line.strip('.\n').split(' ')
                name = words[0]
                speed = float(words[3])
                flyTime = float(words[6])
                restTime = float(words[-2])
                self.AddReindeer(name, speed, flyTime, restTime)


class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime

    def GetPosition(self, time):
        cycleLength = float(self.flyTime + self.restTime)
        fullCycles = math.floor(time / cycleLength)
        fractionalCycles = time % (self.flyTime + self.restTime)
        position = (fullCycles * self.flyTime + min(self.flyTime, fractionalCycles)) * self.speed
        return int(position)

if __name__ == '__main__':
    race = ReindeerRace('input.txt')
    positions = race.GetPositions(2503)
    print 'Part 1: ', max(positions.values())
    race2 = ReindeerRace('input.txt')
    points = race2.GetPoints(2503)
    print 'Part 2: ', max(points.values())
