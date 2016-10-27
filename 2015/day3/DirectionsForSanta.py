def GetUniqueHouses(directions):
    location = [0, 0]
    allLocations = set()
    allLocations.add(tuple(location))
    for direction in directions:
        if direction == '^':
            location[0] += 1
        elif direction == 'v':
            location[0] -= 1
        elif direction == '>':
            location[1] += 1
        elif direction == '<':
            location[1] -= 1
        else:
            raise Exception('Unrecognized direction', direction)
        allLocations.add(tuple(location))
    return allLocations

def TwoSantas(directions):
    santaDirections = GetSantaDirections(directions)
    robotDirections = GetRobotDirections(directions)
    santaHouses = GetUniqueHouses(santaDirections)
    robotHouses = GetUniqueHouses(robotDirections)
    allLocations = santaHouses | robotHouses
    return allLocations


def GetSantaDirections(directions):
    return directions[::2]


def GetRobotDirections(directions):
    return directions[1:][::2]

with open('input.txt', 'r') as f:
    directions = f.read()
    print 'One Santa: ', len(GetUniqueHouses(directions)), '\nTwo Santas: ', len(TwoSantas(directions))
