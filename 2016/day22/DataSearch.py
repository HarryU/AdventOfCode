import numpy as np


class DataNodes:
    def __init__(self):
        self.data_nodes = {}
        self.viable_node_pairs = set()

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                if '/dev/' in line:
                    position, values = self.parse_line(line)
                    self.data_nodes[position] = values

    def parse_line(self, line):
        line = line.strip().split()
        position = tuple(map(int, (line[0].split('-')[1][1:], line[0].split('-')[2][1:])))
        used = int(line[2][:-1])
        empty = int(line[3][:-1])
        return position, {'used': used, 'empty': empty}

    def count_viable_node_pairs(self):
        for node_a in self.data_nodes.keys():
            for node_b in self.data_nodes.keys():
                if self.node_pair_is_viable(node_a, node_b):
                    self.viable_node_pairs.add((node_a, node_b))

    def node_pair_is_viable(self, node_a, node_b):
        if node_a != node_b:
            if self.data_nodes[node_a]['used'] > 0:
                if self.data_nodes[node_a]['used'] < self.data_nodes[node_b]['empty']:
                    return True
        return False

    def show_nodes(self):
        print len(self.data_nodes.keys())
        node_map = np.empty((28, 38), dtype='string')
        for node in self.data_nodes.keys():
            symbol = '.'
            if (0.1 * self.data_nodes[node]['used']) > (0.9 * self.data_nodes[node]['empty']):
                symbol = '#'
            if self.data_nodes[node]['used'] == 0:
                symbol = 'E'
            if node == (0, 0):
                symbol = 'T'
            if node == (37, 0):
                symbol = 'G'
            node_map[node[1], node[0]] = symbol
        np.set_printoptions(threshold=np.nan, linewidth=np.nan)
        print(node_map)


if __name__ == '__main__':
    nodes = DataNodes()
    nodes.parse_file('input')
    nodes.count_viable_node_pairs()
    print('Part 1:', nodes.viable_node_pairs)
    nodes.show_nodes()
