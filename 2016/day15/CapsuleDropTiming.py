def calculateRemainders(t, initStates, discSizes):
    return [(n + t0 + i) % s for n, i, s in zip(range(1, len(discSizes) + 1), initStates, discSizes)]


if __name__ == '__main__':
    t0 = 0
    part1DiscSizes = [7, 13, 3, 5, 17, 19]
    part1InitialStates = [0, 0, 2, 2, 0, 7]
    part2DiscSizes = [7, 13, 3, 5, 17, 19, 11]
    part2InitialStates = [0, 0, 2, 2, 0, 7, 0]
    P1Done = False
    P2Done = False
    while True:
        t0 += 1
        if not P1Done:
            remaindersP1 = calculateRemainders(t0, part1InitialStates, part1DiscSizes)
            if sum(remaindersP1) == 0:
                P1Done = True
                print 'Part 1:', t0
        if not P2Done:
            remaindersP2 = calculateRemainders(t0, part2InitialStates, part2DiscSizes)
            if sum(remaindersP2) == 0:
                P2Done = True
                print 'Part 2:', t0
        if P1Done and P2Done:
            break
