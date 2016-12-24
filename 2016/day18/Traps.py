import unittest


class TestTrapFinder(unittest.TestCase):
    def setUp(self):
        self.traps = Traps([False, False, True, True, False])

    def test_trap_left_centre_safe_right(self):
        self.assertTrue(self.traps.is_trap(True, True, False))

    def test_next_row_generator(self):
        self.traps.gen_next_row()
        self.assertEqual([[False, False, True, True, False],
                          [False, True, True, True, True]], self.traps.traps)

    def test_gen_all_rows(self):
        self.traps.gen_all_rows(3)
        self.assertEqual([[False, False, True, True, False],
                          [False, True, True, True, True],
                          [True, True, False, False, True]], self.traps.traps)

    def test_full_example(self):
        traps = Traps([False, True, True, False, True,
                       False, True, True, True, True])
        traps.gen_all_rows(10)
        self.assertEqual(38, sum([1 for row in traps.traps for x in row if not x]))


class Traps:
    def __init__(self, initial_traps):
        self.traps = [initial_traps]

    def gen_all_rows(self, size):
        while len(self.traps) < size:
            self.gen_next_row()

    def gen_next_row(self):
        current_last_row = self.traps[-1]
        next_row = list()
        for i in range(len(current_last_row)):
            centre_trap = current_last_row[i]
            if i == 0:
                left_trap = False
            else:
                left_trap = current_last_row[i-1]
            if i == len(current_last_row) - 1:
                right_trap = False
            else:
                right_trap = current_last_row[i+1]
            next_row.append(self.is_trap(left_trap, centre_trap, right_trap))
        self.traps.append(next_row)

    def is_trap(self, left_trap, centre_trap, right_trap):
        if (left_trap and centre_trap) and not right_trap:
            return True
        if (centre_trap and right_trap) and not left_trap:
            return True
        if left_trap and not (centre_trap and right_trap):
            return True
        if right_trap and not (centre_trap and left_trap):
            return True
        return False

if __name__ == "__main__":
    puzzle_input = list()
    result = 0
    with open('input', 'r') as f:
        for line in f:
            for char in line.strip():
                puzzle_input.append(char!='.')
    traps = Traps(puzzle_input)
    traps.gen_all_rows(40)
    safe_tile_counts = [row.count(False) for row in traps.traps]
    print(sum(safe_tile_counts))
