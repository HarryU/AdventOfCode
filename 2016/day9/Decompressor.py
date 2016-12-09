import unittest


class TestDecompressor(unittest.TestCase):
    def setUp(self):
        self.decompressor = Decompressor()

    def test_ADVENTDoesntChange(self):
        input = 'ADVENT'
        self.assertEqual(len(input), self.decompressor.decompress(input))

    def test_A1x5BCReturnsCorrectResult(self):
        input = 'A(1x5)BC'
        output = len('ABBBBBC')
        self.assertEqual(output, self.decompressor.decompress(input))

    def test_OtherInputs(self):
        self.assertEqual(len('XYZXYZXYZ'), self.decompressor.decompress('(3x3)XYZ'))
        self.assertEqual(len('ABCBCDEFEFG'), self.decompressor.decompress('A(2x2)BCD(2x2)EFG'))
        self.assertEqual(len('(1x3)A'), self.decompressor.decompress('(6x1)(1x3)A'))
        self.assertEqual(len('X(3x3)ABC(3x3)ABCY'), self.decompressor.decompress('X(8x2)(3x3)ABCY'))
        self.assertEqual(100, self.decompressor.decompress('(1x100)A'))
        self.assertEqual(18, self.decompressor.decompress('X(8x2)(3x3)ABCY'))

    def test_Part2(self):
        self.assertEqual(445, self.decompressor.decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', part2=True))
        self.assertEqual(241920, self.decompressor.decompress('(27x12)(20x12)(13x14)(7x10)(1x12)A', part2=True))


class Decompressor:
    def __init__(self):
        pass

    def decompress(self, string, part2=False):
        string = ''.join(string.split())
        length = 0
        i = 0
        while i < len(string):
            char = string[i]
            if char == '(':
                command = ''
                j = 1
                while string[i + j] is not ')':
                    command += string[i + j]
                    j += 1
                count = int(command.split('x')[0])
                multiple = int(command.split('x')[1])
                dataToRepeat = str(string[i + j + 1:i + j + 1 + count])
                if part2:
                    length += self.decompress(dataToRepeat, part2=True) * multiple
                else:
                    length += len(dataToRepeat) * multiple
                i += j + 1 + count
            else:
                if char != ' ':
                    length += 1
                i += 1
        return length

if __name__ == '__main__':
    decompressor = Decompressor()
    result = 0
    with open('input', 'r') as f:
        for line in f:
            print 'Part 1: ', decompressor.decompress(line)
            print 'Part 2: ', decompressor.decompress(line, True)
