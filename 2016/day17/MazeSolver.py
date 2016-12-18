from hashlib import md5
from itertools import compress
import unittest


class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        self.maze = MazeSolver("hijkl")

    def test_move_up(self):
        current_position = self.maze.move((1, 2), 'U')
        self.assertEqual((1, 1), current_position)

    def test_move_down(self):
        current_position = self.maze.move((1, 1), 'D')
        self.assertEqual((1, 2), current_position)

    def test_move_left(self):
        current_position = self.maze.move((2, 1), 'L')
        self.assertEqual((1, 1), current_position)

    def test_move_right(self):
        current_position = self.maze.move((1, 1), 'R')
        self.assertEqual((2, 1), current_position)

    def test_get_possible_moves(self):
        moves = compress('UDLR', self.maze.get_possible_moves('DU'))
        self.assertEqual(['R'], [x for x in moves])

class MazeSolver:
    def __init__(self, input_string="pvhmgsws"):
        self.input = input_string
        self.directions = {'U': (0, -1),
                           'D': (0, 1),
                           'L': (-1, 0),
                           'R': (1, 0)}
        self.successful_paths = []

    def bfs(self, start_position, target):
        moves = [(start_position, [start_position], [])]
        while len(moves) > 0:
            current_position, path, previous_moves = moves.pop(0)
            for direction in compress('UDLR', self.get_possible_moves(previous_moves)):
                next_x, next_y = self.move(current_position, direction)
                next_position = (next_x, next_y)
                if not (1 <= next_x < 5 and 1 <= next_y < 5):
                    continue
                elif (next_x == 4 and next_y == 4):
                    self.successful_paths.append(previous_moves + [direction])
                else:
                    moves.append((next_position, path + [next_position],
                                  previous_moves + [direction]))
        return self.successful_paths

    def move(self, current_position, direction):
        return (current_position[0] + self.directions[direction][0],
                current_position[1] + self.directions[direction][1])

    def get_possible_moves(self, path):
        string = (self.input + ''.join(path)).encode('utf-8')
        checksum = md5(string).hexdigest()
        return [int(x, 16) > 10 for x in checksum[:4]]

if __name__ == "__main__":
    maze = MazeSolver()
    successful_paths = maze.bfs([1, 1], [4, 4])
    print(''.join(successful_paths[0]), len(successful_paths[-1]))

