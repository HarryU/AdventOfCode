import DirectionsForSanta
import unittest

class DirectionsTests(unittest.TestCase):
    def setUp(self):
        self.testDirections = '^>v<'

    def test_DirectionsExampleInput(self):
        result = DirectionsForSanta.GetUniqueHouses(self.testDirections)
        self.assertEqual(4, len(result))

    def test_TwoSantas(self):
        result = DirectionsForSanta.TwoSantas(self.testDirections)
        self.assertEqual(3, len(result))

    def test_SantaGetsHalfTheDirections(self):
        santaDirections = DirectionsForSanta.GetSantaDirections(self.testDirections)
        self.assertEqual('^v', santaDirections)

    def test_RobotGetsRestOfDirections(self):
        robotDirections = DirectionsForSanta.GetRobotDirections(self.testDirections)
        self.assertEqual('><', robotDirections)
