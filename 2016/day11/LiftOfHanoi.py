class LiftOfHanoi:
    def __init__(self):
        self.currentFloor = 1
        self.floorContents = {1: ['TG', 'TM', 'PG', 'SG'],
                              2: ['PM', 'SM'],
                              3: ['OG', 'OM', 'RG', 'RM'],
                              4: []}

    def move(self, item1, item2):
        floorContents = self.floorContents
        currentFloor = self.currentFloor
        floorContents[currentFloor].remove(item1)
        if item2 is not None:
            floorContents[currentFloor].remove(item2)
        currentFloor += 1
        floorContents[currentFloor].append(item1)
        if item2 is not None:
            floorContents[currentFloor].append(item2)
        if self.unpairedGeneratorAndChipPresent:
            return False
        self.floorContents = floorContents
        self.currentFloor = currentFloor
        return True

    def unpairedGeneratorAndChipPresent(self):
        for item in self.floorContents[self.currentFloor]:
            for otherItem in self.floorContents[self.currentFloor]:
                if item == otherItem:
                    continue
                if item[0] == item[1]:
                    break
                return False

    def chooseMove(self):
        pass