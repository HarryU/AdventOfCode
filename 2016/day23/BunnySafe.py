class Buffer:
    def __init__(self, instructions):
        self.registers = {'a': 12,
                          'b': 0,
                          'c': 0,
                          'd': 0}
        self.i = 0
        self.instructions = instructions

    def processAllInstructions(self):
        while self.i < len(self.instructions):
            self.processInstruction(self.instructions[self.i])

    def processInstruction(self, string):
        stringParts = string.strip().split()
        if 'cpy' in string:
            x = stringParts[1]
            y = stringParts[2]
            self.copy(x, y)
        elif 'inc' in string:
            if stringParts[1] in self.registers.keys():
                if (self.i + 3 < len(self.instructions)) and (self.i - 1 >= 0) and ('cpy' in self.instructions[self.i - 1]) and ('dec' in self.instructions[self.i + 1]) and ('jnz' in self.instructions[self.i + 2]) and ('dec' in self.instructions[self.i + 3]) and ('jnz' in self.instructions[self.i + 4]):
                    copy_source, copy_dest = self.instructions[self.i - 1].split()[1:]
                    first_dec_target = self.instructions[self.i + 1].split()[1]
                    first_jump_condition, first_jump_steps = self.instructions[self.i + 2].split()[1:]
                    second_dec_target = self.instructions[self.i + 3].split()[1]
                    second_jump_condition, second_jump_steps = self.instructions[self.i + 4].split()[1:]
                    if copy_dest == first_dec_target and first_dec_target == first_jump_condition and second_dec_target == second_jump_condition and first_jump_steps == '-2' and second_jump_steps == '-5':
                        if copy_source in self.registers.keys():
                            self.registers[stringParts[1]] += self.registers[copy_source] * self.registers[second_dec_target]
                        else:
                            self.registers[stringParts[1]] += int(copy_source) * self.registers[second_dec_target]
                        self.registers[first_dec_target] = 0
                        self.registers[second_dec_target] = 0
                        self.i += 5
                        return 0
            self.increase(stringParts[1])
        elif 'dec' in string:
            self.decrease(stringParts[1])
        elif 'jnz' in string:
            self.jnz(stringParts[1], stringParts[2])
        elif 'tgl' in string:
            self.toggle(stringParts[1])

    def toggle(self, x):
        if x in self.registers.keys():
            key_to_toggle = self.i + self.registers[x]
        else:
            key_to_toggle = self.i + x
        try:
            instruction_to_toggle = self.instructions[key_to_toggle]
        except IndexError:
            self.i += 1
            return 0
        if len(instruction_to_toggle.strip().split()) == 2:
            if 'inc' in instruction_to_toggle:
                 new_instruction = ''.join(['dec', instruction_to_toggle[3:]])
            else:
                new_instruction = ''.join(['inc', instruction_to_toggle[3:]])
        else:
            if 'jnz' in instruction_to_toggle:
                new_instruction = ''.join(['cpy', instruction_to_toggle[3:]])
            else:
                new_instruction = ''.join(['jnz', instruction_to_toggle[3:]])
        self.instructions[key_to_toggle] = new_instruction
        self.i += 1

    def copy(self, x, y):
        if isinstance(y, int):
            self.i += 1
            return 0
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
        if y in self.registers.keys():
            indexes_to_skip = self.registers[y]
        else:
            indexes_to_skip = int(y)
        if x in self.registers.keys():
            if self.registers[x] != 0:
                self.i += indexes_to_skip
            else:
                self.i += 1
        else:
            if x != 0:
                self.i += indexes_to_skip
            else:
                self.i += 1

if __name__ == '__main__':
    with open('input', 'r') as f:
        instructions = f.readlines()
    buffer = Buffer(instructions)
    # buffer.registers['a'] = 7
    buffer.processAllInstructions()
    print('Part 1:', buffer.registers['a'])
    buffer2 = Buffer(instructions)
    # buffer2.registers['a'] = 12
    buffer2.processAllInstructions()
    print('Part 2:', buffer2.registers['a'])
