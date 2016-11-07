import DistanceCalculator
import unittest


class TestDistanceCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_FirstLineParsing(self):
        destinations = DistanceCalculator.Destinations()
        destinations.ProcessLine('London to Dublin = 464')
        self.assertEqual(464, destinations.destinations['London']['Dublin'])

    def test_PossibleRoutes(self):
        destinations = DistanceCalculator.Destinations('testinput.txt')
        destinations.ProcessFile()
        self.assertEqual(6, len(destinations.PossibleRoutes().keys()))

    def test_ShortestRoute(self):
        destinations = DistanceCalculator.Destinations('testinput.txt')
        destinations.ProcessFile()
        routes = destinations.PossibleRoutes()
        self.assertEqual(605, min(routes.values()))
