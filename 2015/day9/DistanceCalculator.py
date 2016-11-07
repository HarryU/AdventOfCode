from itertools import permutations


class Destinations:
    def __init__(self, filename='input.txt'):
        self.filename = filename
        self.destinations = dict()

    def ProcessFile(self):
        with open(self.filename, 'r') as input:
            for line in input:
                self.ProcessLine(line)

    def ProcessLine(self, line):
        words = line.split(' ')
        destination1 = words[0]
        destination2 = words[2]
        distance = words[-1]
        if destination1 not in self.destinations.keys():
            self.destinations[destination1] = {}
        if destination2 not in self.destinations.keys():
            self.destinations[destination2] = {}
        self.destinations[destination1][destination2] = int(distance)
        self.destinations[destination2][destination1] = int(distance)

    def PossibleRoutes(self):
        routes = dict()
        for order in permutations(self.destinations.keys()):
            distance = 0
            for i in range(len(order) - 1):
                destination1 = order[i]
                destination2 = order[i + 1]
                distance += self.destinations[destination1][destination2]
            routes[order] = distance
        return routes

if __name__ == '__main__':
    destinations = Destinations('input.txt')
    destinations.ProcessFile()
    print min(destinations.PossibleRoutes().values())
    print max(destinations.PossibleRoutes().values())