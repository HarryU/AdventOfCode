import unittest


class TestDragonChecksum(unittest.TestCase):
    def setUp(self):
        self.checksum = DragonChecksum()

    def test_ApplyDragonCurve(self):
        self.assertEqual('100', self.checksum.ApplyDragonCurve('1'))


class DragonChecksum:
    def __init__(self):
        pass

    def ApplyDragonCurve(self, input):
        output = input
        return ouput
