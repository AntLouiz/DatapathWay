class MipsInstruction:
    op = None
    rs = None
    rt = None
    rd = None
    shamt = None
    func = None
    offset = None
    instruction_type = None
    instruction = None

    def __init__(self, instruction):
        if not (isinstance(instruction, str) or len(instruction) == 32):
            raise Exception()

        self.instruction = instruction
        self.op = self.instruction[:6]

        if self.op == '000000':
            self.instruction_type = 'R'
            self.rs = self.instruction[6:11]
            self.rt = self.instruction[11:16]
            self.rd = self.instruction[16:21]
            self.shamt = self.instruction[21:26]
            self.func = self.instruction[26:32]

        else:
            pass

    def has_offset(self):
        if self.instruction_type == 'R':
            return False

        return True

    def get_type(self):
        return self.instruction_type

    def _check_instruction(self):
        pass

    def __repr__(self):
        return "Instruction: {} \nType: {}".format(
            self.instruction,
            self.instruction_type
        )


class PC:
    def __init__(self, filename="instructions_file.txt"):
        self.file = open(filename, 'r')
        self.next_instruction = None

    def get_instructions(self):
        """
        Return a mips instruction object
        for each instruction in the file
        """

        for instruction in self.file.readlines():
            if self.next_instruction:
                self.next_instruction = MipsInstruction(instruction)
            else:
                self.next_instruction = MipsInstruction(instruction)

            yield self.next_instruction
