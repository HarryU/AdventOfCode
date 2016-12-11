import unittest


class TestRobotRoleFinding(unittest.TestCase):
    def setUp(self):
        self.roles = RobotRoles()
        self.roles.parseValueLine('value 5 goes to bot 2')
        self.roles.parseInstructionLine('bot 2 gives low to bot 1 and high to bot 0')
        self.roles.parseValueLine('value 3 goes to bot 1')
        self.roles.parseInstructionLine('bot 1 gives low to output 1 and high to bot 0')
        self.roles.parseInstructionLine('bot 0 gives low to output 2 and high to output 0')
        self.roles.parseValueLine('value 2 goes to bot 2')

    def test_LinesAreParsedCorrectly(self):
        self.assertTrue(5 in self.roles.robots[2].microchips)
        self.assertEqual(1, self.roles.robots[2].targetLow)
        self.assertEqual(0, self.roles.robots[2].targetHigh)
        self.assertEqual(3, self.roles.robots[1].microchips[0])
        self.assertEqual(1, self.roles.robots[1].targetLow)
        self.assertEqual(0, self.roles.robots[1].targetHigh)
        self.assertTrue(self.roles.robots[1].lowIsOutput)
        self.assertEqual(2, self.roles.robots[0].targetLow)
        self.assertEqual(0, self.roles.robots[0].targetHigh)
        self.assertTrue(self.roles.robots[0].lowIsOutput)
        self.assertTrue(self.roles.robots[0].highIsOutput)
        self.assertTrue(2 in self.roles.robots[2].microchips)

    def test_ConnectingRobots(self):
        self.roles.connectRobots()
        print self.roles.robots[0]


class Robot:
    def __init__(self, botNumber, targetLow, targetHigh, lowIsOutput=False, highIsOutput=False):
        self.botNumber = botNumber
        self.microchips = set()
        self.targetLow = targetLow
        self.lowIsOutput = lowIsOutput
        self.targetHigh = targetHigh
        self.highIsOutput = highIsOutput

    def allAttributesSet(self):
        allAttrSet = all([isinstance(self.botNumber, int), len(self.microchips) >= 2, self.targetLow is not None, self.targetHigh is not None])
        return allAttrSet


class RobotRoles:
    def __init__(self):
        self.robots = {}
        self.instructionLines = []
        self.outputs = {}

    def parseFile(self, fileObj):
        for line in fileObj:
            line = line.strip()
            if 'value' in line:
                self.parseValueLine(line)
            else:
                self.instructionLines.append(line)
        for line in self.instructionLines:
            line = line.strip()
            self.parseInstructionLine(line)
        self.connectRobots()

    def parseValueLine(self, string):
        stringParts = string.split()
        chipNumber = int(stringParts[1])
        botNumber = int(stringParts[-1])
        if botNumber in self.robots.keys():
            self.robots[botNumber].microchips.add(chipNumber)
        else:
            self.robots[botNumber] = Robot(botNumber, None, None)
            self.robots[botNumber].microchips.add(chipNumber)

    def parseInstructionLine(self, string):
        stringParts = string.split()
        bot = int(stringParts[1])
        targetLow = int(stringParts[6])
        targetHigh = int(stringParts[11])
        lowIsOutput = False
        highIsOutput = False
        if stringParts[5] == 'output':
            lowIsOutput = True
        if stringParts[10] == 'output':
            highIsOutput = True
        if bot in self.robots.keys():
            self.robots[bot].targetLow = targetLow
            self.robots[bot].targetHigh = targetHigh
            self.robots[bot].highIsOutput = highIsOutput
            self.robots[bot].lowIsOutput = lowIsOutput
        else:
            self.robots[bot] = Robot(bot, targetLow=targetLow, targetHigh=targetHigh, lowIsOutput=lowIsOutput, highIsOutput=highIsOutput)

    def connectRobots(self):
        robotsToSort = self.robots.values()
        doneRobots = []
        while len(doneRobots) < len(robotsToSort):
            for robot in robotsToSort:
                if robot in doneRobots:
                    continue
                if len(robot.microchips) == 2:
                    if robot.lowIsOutput:
                        self.outputs[robot.targetLow] = min(robot.microchips)
                    else:
                        if robot.targetLow in self.robots.keys():
                            self.robots[robot.targetLow].microchips.add(min(robot.microchips))
                        else:
                            self.robots[robot.targetLow] = Robot(botNumber=robot.targetLow, targetLow=None, targetHigh=None)
                            self.robots[robot.targetLow].microchips.add(min(robot.microchips))
                    if robot.highIsOutput:
                        self.outputs[robot.targetHigh] = max(robot.microchips)
                    else:
                        if robot.targetHigh in self.robots.keys():
                            self.robots[robot.targetHigh].microchips.add(max(robot.microchips))
                        else:
                            self.robots[robot.targetHigh] = Robot(robot.targetHigh, None, None)
                            self.robots[robot.robot.targetHigh].microchips.add(max(robot.microchips))
                if robot.allAttributesSet():
                    doneRobots.append(robot)

if __name__ == '__main__':
    roles = RobotRoles()
    with open('input', 'r') as f:
        roles.parseFile(f)
        for robot in roles.robots.values():
            if (61 in robot.microchips) and (17 in robot.microchips):
                print 'Part 1: ', robot.botNumber
        print 'Part 2: ', roles.outputs[0] * roles.outputs[1] * roles.outputs[2]