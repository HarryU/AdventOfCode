class Circuit(object):
    def __init__(self):
        self.circuit = {}

    def Assign(self, value, wire):
        if not str(value).isdigit():
            if value in self.circuit.keys():
                self.circuit[wire] = self.Get(value)
            else:
                return 1
        else:
            self.circuit[wire] = int(value)

    def Get(self, wire):
        return int(self.circuit[wire])

    def And(self, value1, value2):
        if not str(value1).isdigit():
            if value1 in self.circuit.keys():
                value1 = self.circuit[value1]
            else:
                return 'INVALID'
        if not str(value2).isdigit():
            if value2 in self.circuit.keys():
                value2 = self.circuit[value2]
            else:
                return 'INVALID'
        return (int(value1) & 65535) & (int(value2) & 65535)

    def Or(self, value1, value2):
        return (self.Get(value1) & 65535) | (self.Get(value2) & 65535)

    def LShift(self, wire, amount):
        return ((self.Get(wire) & 65535) << int(amount)) & 65535

    def RShift(self, wire, amount):
        return ((self.Get(wire) & 65535) >> int(amount)) & 65535

    def Not(self, wire):
        return ~(self.Get(wire) & 65535) & 65535


class Parser(object):
    def __init__(self):
        self.instructions = {}

    def Process(self, line):
        words = line.split(' ')
        targetWire = words[-1].strip('\n')
        if len(words) == 3:
            # Instruction is a simple assignment
            self.instructions[targetWire] = 'Assign ' + words[0]
        if len(words) == 4:
            # Instruction is a simple not
            self.instructions[targetWire] = 'Not ' + words[1]
        if len(words) == 5:
            if 'LSHIFT' in words:
                self.instructions[targetWire] = 'Lshift ' + words[0] + ' ' + words[2]
            elif 'RSHIFT' in words:
                self.instructions[targetWire] = 'Rshift ' + words[0] + ' ' + words[2]
            elif 'AND' in words:
                self.instructions[targetWire] = 'And ' + words[0] + ' ' + words[2]
            elif 'OR' in words:
                self.instructions[targetWire] = 'Or ' + words[0] + ' ' + words[2]


def ProcessInput(instructions, circuitObject):
    newInstructions = {}
    for wire in sorted(instructions.keys()):
        instruction = instructions[wire].split(' ')
        if 'Assign' in instruction:
            if circuitObject.Assign(instruction[-1], wire) == 1:
                newInstructions[wire] = instructions[wire]
                continue
        elif 'And' in instruction:
            if circuitObject.And(instruction[1], instruction[2]) == 'INVALID':
                newInstructions[wire] = instructions[wire]
                continue
            circuitObject.Assign(circuitObject.And(instruction[1], instruction[2]), wire)
        elif 'Or' in instruction:
            if (instruction[1] not in circuitObject.circuit.keys()) or (instruction[2] not in circuitObject.circuit.keys()):
                newInstructions[wire] = instructions[wire]
                continue
            circuitObject.Assign(circuitObject.Or(instruction[1], instruction[2]), wire)
        elif 'Lshift' in instruction:
            if instruction[1] not in circuitObject.circuit.keys():
                newInstructions[wire] = instructions[wire]
                continue
            circuitObject.Assign(circuitObject.LShift(instruction[1], instruction[2]), wire)
        elif 'Rshift' in instruction:
            if instruction[1] not in circuitObject.circuit.keys():
                newInstructions[wire] = instructions[wire]
                continue
            circuitObject.Assign(circuitObject.RShift(instruction[1], instruction[2]), wire)
        elif 'Not' in instruction:
            if instruction[1] not in circuitObject.circuit.keys():
                newInstructions[wire] = instructions[wire]
                continue
            circuitObject.Assign(circuitObject.Not(instruction[1]), wire)
    if len(newInstructions.keys()) > 0:
        ProcessInput(newInstructions, circuitObject)

if __name__ == '__main__':
    circuit = Circuit()
    parser = Parser()
    with open('input.txt', 'r') as input:
        for line in input:
            parser.Process(line)
    ProcessInput(parser.instructions, circuit)
    print 'Part 1: ', circuit.Get('a')
    part2Circuit = Circuit()
    part2Parser = Parser()
    with open('input2.txt', 'r') as input:
        for line in input:
            part2Parser.Process(line)
    ProcessInput(part2Parser.instructions, part2Circuit)
    print 'Part 2: ', part2Circuit.Get('a')
