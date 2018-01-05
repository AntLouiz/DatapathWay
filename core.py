class MipsInstruction:
    op = None
    rs = None
    rt = None
    rd = None
    shamt = None
    func = None
    offset = None
    instruction_type = None

    def __init__(self, instruction):
        pass

    def has_offset(self):
        pass

    def get_type(self):
        return self.instruction_type

    def _check_instruction(self):
        pass


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
