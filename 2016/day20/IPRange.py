import unittest


class TestIPRange(unittest.TestCase):
    def setUp(self):
        self.ranges = IPRange()

    def test_add_ip_range(self):
        self.ranges.add_range(5, 8)
        self.assertEqual([[5, 8]], self.ranges.ranges)

    def test_add_2nd_ip_range(self):
        self.ranges.add_range(5, 8)
        self.ranges.add_range(0, 2)
        self.assertEqual([[0, 2], [5, 8]], self.ranges.ranges)

    def test_join_overlapping_ranges(self):
        self.ranges.add_range(5, 8)
        self.ranges.add_range(0, 2)
        self.ranges.add_range(4, 7)
        self.assertEqual([[0, 2], [4, 8]], self.ranges.ranges)

    def test_find_possible_ip_addresses(self):
        self.ranges.add_range(5, 8)
        self.ranges.add_range(0, 2)
        self.ranges.add_range(4, 7)
        self.assertEqual(3, self.ranges.lowest_possible_ip_address())

    def test_touching_ranges_collapse(self):
        self.ranges.add_range(0, 2)
        self.ranges.add_range(3, 5)
        self.ranges.collapse_ranges()
        self.assertEqual([[0, 5]], self.ranges.ranges)

    def test_real_input(self):
        with open('input', 'r') as f:
            for line in f:
                range_lower, range_upper = map(int, line.strip().split('-'))
                self.ranges.add_range(range_lower, range_upper)
        self.ranges.collapse_ranges()
        self.assertEqual(22887907, self.ranges.lowest_possible_ip_address())
        self.assertEqual(109, self.ranges.count_allowed_ips())

    def test_allowed_ips(self):
        self.ranges.add_range(5, 8)
        self.ranges.add_range(0, 2)
        self.ranges.add_range(4, 7)
        self.ranges.collapse_ranges()
        self.assertEqual(2, self.ranges.count_allowed_ips(9))


class IPRange:
    def __init__(self):
        self._ranges = list()

    @property
    def ranges(self):
        self.collapse_ranges()
        return self._ranges

    def add_range(self, start, stop):
        self._ranges.append([start, stop])

    def collapse_ranges(self):
        self._ranges.sort()
        collapsed = []
        for range_lower, range_upper in self._ranges:
            for collapsed_range in collapsed:
                if range_lower <= collapsed_range[1] + 1:
                    if collapsed_range[1] <= range_upper:
                        collapsed_range[1] = range_upper
                    break
            else:
                collapsed.append([range_lower, range_upper])
        self._ranges = collapsed

    def lowest_possible_ip_address(self):
        return range(self.ranges[0][1] + 1, self.ranges[1][0])[0]

    def count_allowed_ips(self, max=4294967295):
        return max + 1 - sum([(upper + 1 - lower) for lower, upper in self.ranges])
