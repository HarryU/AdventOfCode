from collections import deque

elves = deque()
puzzle_input = 9
for i in range(puzzle_input):
    elves.append(i)


def solve():
    while len(elves) > 1:
        i = elves.popleft()
        _ = elves.popleft()
        elves.append(i)
    return list(elves)[0] + 1


first_half_of_elves = deque()
second_half_of_elves = deque()
for i in range(1, puzzle_input + 1):
    if i < (puzzle_input // 2) + 1:
        first_half_of_elves.append(i)
    else:
        second_half_of_elves.appendleft(i)


def solve_part_2():
    while first_half_of_elves and second_half_of_elves:
        print(first_half_of_elves, second_half_of_elves)
        if len(first_half_of_elves) > len(second_half_of_elves):
            first_half_of_elves.pop()
        else:
            second_half_of_elves.pop()

        second_half_of_elves.appendleft(first_half_of_elves.popleft())
        first_half_of_elves.append(second_half_of_elves.pop())
    return first_half_of_elves[0] or second_half_of_elves[0]


print("Part 1:", solve())
print("Part 2:", solve_part_2())
