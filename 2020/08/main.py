class CPU:
    def __init__(self, program):
        self.history = []
        self.stack_trace = []

        self.acc = 0
        self.pc = 0

        self.opcodes = {
            'nop': self.nop_impl,
            'acc': self.acc_impl,
            'jmp': self.jmp_impl
        }

        self.program = program

    def start(self):
        while self.pc < len(self.program):
            if self.pc in self.history:
                print(f'Infinite Loop. Current acc: {self.acc}')
                return

            self.step()

        print(f'Program Exited. Current acc: {self.acc}')

    def step(self):
        opcode, arg = self.program[self.pc]

        self.history.append(self.pc)
        self.stack_trace.append(f'{opcode} {arg}')

        self.pc += 1
        self.opcodes[opcode](arg)

    def nop_impl(self, arg):
        pass

    def acc_impl(self, arg):
        self.acc += arg

    def jmp_impl(self, arg):
        self.pc += arg - 1


program = []

for instruction in open(f"program.txt").readlines():
    opcode, arg = instruction.split(' ')
    program += [(opcode, int(arg))]

cpu = CPU(program)
cpu.start()

for line in range(len(program)):
    new_program = list(program)
    if new_program[line][0] == 'nop':
        new_program[line] = ('jmp', new_program[line][1])
    if new_program[line][0] == 'jmp':
        new_program[line] = ('nop', new_program[line][1])
    else:
        continue

    cpu = CPU(new_program)
    cpu.start()
