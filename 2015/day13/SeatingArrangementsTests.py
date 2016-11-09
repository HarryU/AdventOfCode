import SeatingArrangements
import unittest


class TestSeatingArragements(unittest.TestCase):
    def setUp(self):
        pass

    def test_FileParsingToDict(self):
        seating = SeatingArrangements.SeatPlan('testInput.txt')
        self.assertEqual(54, seating.GetHappinessChange('Alice', 'Bob'))
        self.assertEqual(-2, seating.GetHappinessChange('Alice', 'David'))
        self.assertEqual(83, seating.GetHappinessChange('Bob', 'Alice'))
        self.assertEqual(-7, seating.GetHappinessChange('Bob', 'Carol'))
        self.assertEqual(60, seating.GetHappinessChange('Carol', 'Bob'))
        self.assertEqual(55, seating.GetHappinessChange('Carol', 'David'))
        self.assertEqual(41, seating.GetHappinessChange('David', 'Carol'))
        self.assertEqual(46, seating.GetHappinessChange('David', 'Alice'))

    def test_CalculateTotalHappinessOfArrangment(self):
        seating = SeatingArrangements.SeatPlan('testInput.txt')
        self.assertEqual(330, seating.TotalHappiness(['David', 'Alice', 'Bob', 'Carol']))

    def test_GetAllSeatingArrangements(self):
        seating = SeatingArrangements.SeatPlan('testInput.txt')
        happinessValues = list()
        for order in seating.GetAllSeatingOrders():
            happinessValues.append(seating.TotalHappiness(order))
        self.assertEqual(330, max(happinessValues))
