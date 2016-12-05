import numpy as np


class ChristmasLights:
    def __init__(self):
        self.lights = np.zeros((1000, 1000))

    def Change(self, instruction):
        words = instruction.split(' ')
        if 'toggle' in words:
            self.Toggle(words[1], words[-1])
        elif 'on' in words:
            self.TurnOn(words[2], words[-1])
        elif 'off' in words:
            self.TurnOff(words[2], words[-1])

    def ChangePart1(self, instruction):
        words = instruction.split(' ')
        if 'toggle' in words:
            self.TogglePart1(words[1], words[-1])
        elif 'on' in words:
            self.TurnOnPart1(words[2], words[-1])
        elif 'off' in words:
            self.TurnOffPart1(words[2], words[-1])

    def Toggle(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY] += 2

    def TogglePart1(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY] = 1 - self.lights[startX:stopX, startY:stopY]

    def TurnOn(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY] += 1

    def TurnOnPart1(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY] = 1

    def TurnOff(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY][np.where(self.lights[startX:stopX, startY:stopY] > 0)] = \
        (self.lights[startX:stopX, startY:stopY] - 1)[np.where(self.lights[startX:stopX, startY:stopY] > 0)]

    def TurnOffPart1(self, start, stop):
        startX, startY, stopX, stopY = self.GetIndices(start, stop)
        self.lights[startX:stopX, startY:stopY] = 0

    def GetIndices(self, start, stop):
        startX = int(start.split(',')[0])
        startY = int(start.split(',')[1])
        stopX = int(stop.split(',')[0]) + 1
        stopY = int(stop.split(',')[1]) + 1
        return startX, startY, stopX, stopY


christmasLights = ChristmasLights()

with open('input.txt', 'r') as f:
    for line in f:
        christmasLights.Change(line)
print np.sum(christmasLights.lights)
