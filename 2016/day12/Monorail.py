class Buffer:
    def __init__(self):
        self.registers = {'a': 0,
                          'b': 0,
                          'c': 0,
                          'd': 0}
        self.i = 0

    def processAllInstructions(self, instructions):
        while self.i < len(instructions):
            self.processInstruction(instructions[self.i])

    def processInstruction(self, string):
        stringParts = string.strip().split()
        if 'cpy' in string:
            x = stringParts[1]
            y = stringParts[2]
            self.copy(x, y)
        elif 'inc' in string:
            self.increase(stringParts[1])
        elif 'dec' in string:
            self.decrease(stringParts[1])
        elif 'jnz' in string:
            self.jnz(stringParts[1], stringParts[2])

    def copy(self, x, y):
        try:
            x = int(x)
            self.registers[y] = x
        except ValueError:
            self.registers[y] = self.registers[x]
        self.i += 1

    def increase(self, x):
        self.registers[x] += 1
        self.i += 1

    def decrease(self, x):
        self.registers[x] -= 1
        self.i += 1

    def jnz(self, x, y):
        if x in self.registers.keys():
            if self.registers[x] != 0:
                self.i += int(y)
            else:
                self.i += 1
        else:
            if x != 0:
                self.i += int(y)
            else:
                self.i += 1

if __name__ == '__main__':
    buffer = Buffer()
    with open('input', 'r') as f:
        instructions = f.readlines()
        buffer.processAllInstructions(instructions)
    print buffer.registers['a']
    bufferPart2 = Buffer()
    with open('input', 'r') as f:
        instructions = f.readlines()
        bufferPart2.registers['c'] = 1
        bufferPart2.processAllInstructions(instructions)
    print bufferPart2.registers['a']
