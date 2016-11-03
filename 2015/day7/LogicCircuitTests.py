import LogicCircuits
import unittest

class LogicCircuitTests(unittest.TestCase):
    def setUp(self):
        self.circuit = LogicCircuits.Circuit()
        self.circuit.Assign(123, 'x')
        self.circuit.Assign(456, 'y')
        self.circuit.Assign(self.circuit.And('x', 'y'), 'd')
        self.circuit.Assign(self.circuit.Or('x', 'y'), 'e')
        self.circuit.Assign(self.circuit.LShift('x', 2), 'f')
        self.circuit.Assign(self.circuit.RShift('y', 2), 'g')
        self.circuit.Assign(self.circuit.Not('x'), 'h')
        self.circuit.Assign(self.circuit.Not('y'), 'i')
        self.parser = LogicCircuits.Parser()
        with open('testInput.txt', 'r') as testInput:
            for line in testInput:
                self.parser.Process(line)

    def test_WireReturnsCorrectResultAfterAssignment(self):
        self.assertEqual(123, self.circuit.Get('x'))

    def test_xAndyReturnsCorrectResult(self):
        self.assertEqual(72, self.circuit.Get('d'))

    def test_xOryReturnsCorrectResult(self):
        self.assertEqual(507, self.circuit.Get('e'))

    def test_LSHIFTxBy2(self):
        self.assertEqual(492, self.circuit.Get('f'))

    def test_RSHIFTyBy2(self):
        self.assertEqual(114, self.circuit.Get('g'))

    def test_Notx(self):
        self.assertEqual(65412, self.circuit.Get('h'))

    def test_Noty(self):
        self.assertEqual(65079, self.circuit.Get('i'))

    def test_InputParsing(self):
        self.assertEqual('Assign 123', self.parser.instructions['x'])

    def test_InputProcessing(self):
        circuit = LogicCircuits.Circuit()
        LogicCircuits.ProcessInput(self.parser.instructions, circuit)
        self.assertEqual(123, circuit.Get('x'))
        self.assertEqual(456, circuit.Get('y'))
        self.assertEqual(72, circuit.Get('d'))
        self.assertEqual(507, circuit.Get('e'))
        self.assertEqual(492, circuit.Get('f'))
        self.assertEqual(114, circuit.Get('g'))
        self.assertEqual(65412, circuit.Get('h'))
        self.assertEqual(65079, circuit.Get('i'))


