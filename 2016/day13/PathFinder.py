import numpy as np

class Map:
    def __init__(self, n):
        self.map = np.zeros((n, n))

    def fillMap(self, puzzleInput=1364):
        for y in self.map.shape[0]:
            for x in self.map.shape[1]:
                equation = (x**2) + (3*x) + (2*x*y) + y + (y**2) + puzzleInput
                binary = format(equation, 'b')
