class Cpu:
    pc = 0

    def __init__(self, code, debug=False):
        self.debug = debug
        self.code = code.copy()
        self.memory = code.copy()

    def log(self, msg):
        if self.debug:
            print(msg)

    def reset(self):
        self.pc = 0
        self.memory = self.code.copy()

    def flash(self, memory):
        self.log(f'Flash new memory: {memory}')
        self.code = memory.copy()
        self.memory = memory.copy()
        self.pc = 0

    def run(self):
        running = True
        while running:
            running = self.step()

        memory = self.memory
        self.reset()
        return memory

    def step(self):
        try:
            opcode = self.memory[self.pc]

            if opcode == 1:
                adress1 = self.memory[self.pc + 1]
                adress2 = self.memory[self.pc + 2]
                adress3 = self.memory[self.pc + 3]
                self.memory[adress3] = self.memory[adress1] + self.memory[adress2]
                self.pc += 4

                self.log(
                    f'Running opcode {opcode} with arguments {adress1},{adress2},{adress3}. Result: {self.memory[adress3]}')
            if opcode == 2:
                adress1 = self.memory[self.pc + 1]
                adress2 = self.memory[self.pc + 2]
                adress3 = self.memory[self.pc + 3]
                self.memory[adress3] = self.memory[adress1] * self.memory[adress2]
                self.pc += 4

                self.log(
                    f'Running opcode {opcode} with arguments {adress1},{adress2},{adress3}. Result: {self.memory[adress3]}')
            if opcode == 99:
                self.pc += 1
                
                self.log('Halt')
                return False

            return True
        except Exception as e:
            self.log(f'Exception: {e}')
            return False
