import HouseDelivery
import unittest


class TestHouseDelivery(unittest.TestCase):
    def setUp(self):
        pass

    def test_GetFactors12(self):
        factorsOfTwelve = {1, 12, 2, 6, 3, 4}
        self.assertEqual(factorsOfTwelve, HouseDelivery.getFactors(12))

    def test_GetFactors9(self):
        factorsOfTwelve = {1, 9, 3, 3}
        self.assertEqual(factorsOfTwelve, HouseDelivery.getFactors(9))

    def test_8GetsRightPresents(self):
        self.assertEqual(150, HouseDelivery.totalPresents(8))

    def test_9GetsRightNumberOfPresents(self):
        self.assertEqual(130, HouseDelivery.totalPresents(9))
