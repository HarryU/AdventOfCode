import unittest


class TestTrapFinder(unittest.TestCase):
    def setUp(self):
        self.traps = Traps([False, False, True, True, False])

    def test_trap_left_centre_safe_right(self):
        self.assertTrue(self.traps.is_trap(True, True, False))


class Traps:
    def __init__(self, initial_traps):
        self.traps = [initial_traps]

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


