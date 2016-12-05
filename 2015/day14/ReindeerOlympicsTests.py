import ReindeerOlympics
import unittest


class TestReindeerOlympics(unittest.TestCase):
    def setUp(self):
        self.filename = 'testInput.txt'

    def test_DistanceComet(self):
        comet = ReindeerOlympics.Reindeer('comet', 14, 10, 127)
        self.assertEqual(14, comet.GetPosition(1))
        self.assertEqual(140, comet.GetPosition(10))
        self.assertEqual(140, comet.GetPosition(12))
        self.assertEqual(1120, comet.GetPosition(1000))

    def test_ParsingFile(self):
        race = ReindeerOlympics.ReindeerRace(self.filename)
        testValues = [ReindeerOlympics.Reindeer('Comet', 14, 10, 127),
                      ReindeerOlympics.Reindeer('Dancer', 16, 11, 162)]
        self.assertEqual(race.allReindeer[0].__dict__, testValues[0].__dict__)
        self.assertEqual(race.allReindeer[1].__dict__, testValues[1].__dict__)

    def test_RacePositionsAt1000s(self):
        race = ReindeerOlympics.ReindeerRace(self.filename)
        positions = race.GetPositions(1000)
        self.assertEqual(1120, positions['Comet'])
        self.assertEqual(1056, positions['Dancer'])

    def test_Part2PointsAt140s(self):
        race = ReindeerOlympics.ReindeerRace(self.filename)
        points = race.GetPoints(140)
        self.assertEqual(139, points['Dancer'])
        self.assertEqual(1, points['Comet'])

    def test_Part2PointsAt10s(self):
        race = ReindeerOlympics.ReindeerRace(self.filename)
        points = race.GetPoints(10)
        self.assertEqual(10, points['Dancer'])
        self.assertEqual(0, points['Comet'])

    def test_Part2PointsInRealInput(self):
        race = ReindeerOlympics.ReindeerRace('input.txt')
        points = race.GetPoints(2503)
        print points

    def test_Part2PointsAt1000s(self):
        race = ReindeerOlympics.ReindeerRace(self.filename)
        points = race.GetPoints(1000)
        self.assertEqual(689, points['Dancer'])
        self.assertEqual(312, points['Comet'])
