from collections import deque
from itertools import permutations
from mock import patch
import unittest

run_long_tests = False


class TestPasswordScrambler(unittest.TestCase):
    def setUp(self):
        self.scrambler = PasswordScrambler('abcde')

    def test_swap_index_x_and_y(self):
        x = 4
        y = 0
        input = 'abcde'
        expected_output = 'ebcda'
        self.assertEqual(expected_output, self.scrambler.swap_index(input, x, y))

    def test_swap_value_x_and_y(self):
        x = 'd'
        y = 'b'
        input = 'ebcda'
        expected_output = 'edcba'
        self.assertEqual(expected_output, self.scrambler.swap_value(input, x, y))

    def test_reverse_x_through_y(self):
        x = 0
        y = 4
        input = 'edcba'
        expected_output = 'abcde'
        self.assertEqual(expected_output, self.scrambler.reverse(input, x, y))

    def test_rotate_left_x_steps(self):
        x = 1
        direction = 'L'
        input = 'abcde'
        expected_output = 'bcdea'
        self.assertEqual(expected_output, self.scrambler.rotate_by_steps(input, x, direction))

    def test_move_position_x_to_y(self):
        x = 1
        y = 4
        input = 'bcdea'
        expected_output = 'bdeac'
        self.assertEqual(expected_output, self.scrambler.move(input, x, y))

    def test_rotate_based_on_letter_position(self):
        x = 'd'
        input = 'ecabd'
        expected_output = 'decab'
        self.assertEqual(expected_output, self.scrambler.rotate_based_on_char(input, x))

    def test_line_parsing(self):
        line = 'swap position 4 with position 0'
        with patch.object(self.scrambler, 'swap_index') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 4, 0)
        line = 'swap letter d with letter b'
        with patch.object(self.scrambler, 'swap_value') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 'd', 'b')
        line = 'reverse positions 0 through 4'
        with patch.object(self.scrambler, 'reverse') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 0, 4)
        line = 'rotate left 1 step'
        with patch.object(self.scrambler, 'rotate_by_steps') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 1, 'L')
        line = 'rotate right 3 steps'
        with patch.object(self.scrambler, 'rotate_by_steps') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 3, 'R')
        line = 'move position 1 to position 4'
        with patch.object(self.scrambler, 'move') as mock:
            self.scrambler.parse(line)
            mock.assert_called_with('abcde', 1, 4)

    @unittest.skipUnless(run_long_tests, 'Skipping bruteforce unscramble because it takes a long time to run.')
    def test_reverse_scrambled_password(self):
        unscrambler = PasswordScrambler()
        self.assertEqual('abcdefgh', unscrambler.unscramble('gbhcefad'))

    def test_real_input(self):
        real_scrambler = PasswordScrambler()
        with open('input', 'r') as f:
            for line in f:
                real_scrambler.string = real_scrambler.parse(line)
        self.assertEqual('gbhcefad', real_scrambler.string)
        self.assertEqual('gahedfcb', real_scrambler.unscramble('fbgdceah'))


class PasswordScrambler:
    def __init__(self, input_string='abcdefgh'):
        self.string = input_string

    def parse(self, line):
        line = line.strip().split()
        if 'swap' in line:
            if 'position' in line:
                new_string = self.swap_index(self.string, int(line[2]), int(line[-1]))
            else:
                new_string = self.swap_value(self.string, line[2], line[-1])
        elif 'reverse' in line:
            new_string = self.reverse(self.string, int(line[2]), int(line[-1]))
        elif 'rotate' in line:
            if 'step' in line[-1]:
                new_string = self.rotate_by_steps(self.string, int(line[2]), ('L' if line[1] == 'left' else 'R'))
            else:
                new_string = self.rotate_based_on_char(self.string, line[-1])
        elif 'move' in line:
            new_string = self.move(self.string, int(line[2]), int(line[5]))
        else:
            raise ValueError(''.join(line), ' is not a recognized instruction.')
        return new_string

    def swap_index(self, string, swap_from, swap_to):
        new_string = list(string)
        new_string[swap_from] = string[swap_to]
        new_string[swap_to] = string[swap_from]
        return ''.join(new_string)

    def swap_value(self, string, from_value, to_value):
        from_index = list(string).index(from_value)
        to_index = list(string).index(to_value)
        return self.swap_index(string, from_index, to_index)

    def reverse(self, string, from_index, to_index):
        new_string = list(string)
        new_string[from_index:to_index + 1] = list(string)[from_index:to_index + 1][::-1]
        return ''.join(new_string)

    def rotate_by_steps(self, string, n_steps, direction='R'):
        if direction == 'L':
            n_steps = -n_steps
        new_string = deque(string)
        new_string.rotate(n_steps)
        return ''.join(new_string)

    def move(self, string, from_position, to_position):
        new_string = list(string)
        char = new_string[from_position]
        del new_string[from_position]
        new_string.insert(to_position, char)
        return ''.join(new_string)

    def rotate_based_on_char(self, string, char):
        n_steps = 1 + string.index(char) + (1 if string.index(char) >= 4 else 0)
        return self.rotate_by_steps(string, n_steps)

    def unscramble(self, string):
        for candidate_password in [''.join(candidate_password) for candidate_password in permutations(string)]:
            self.string = candidate_password
            with open('input', 'r') as f:
                for line in f:
                    self.string = self.parse(line)
            if self.string == string:
                break
        else:
            raise ValueError(candidate_password, 'could not be inverted with these instructions.')
        return(candidate_password)
