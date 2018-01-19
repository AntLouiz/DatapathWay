from li import FUNCTIONS
from utils import extend_to_bits

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

        self.instruction = instruction.replace('\n', '')
        self.op = self.instruction[:6]

        if self.op == '000000':
            self._configure_to_registers()
        else:
            self._configure_to_imediate()

    def _configure_to_imediate(self):
            self.instruction_type = 'I'
            self.rs = self.instruction[6:11]
            self.rt = self.instruction[11:16]
            self.offset = self.instruction[16:32]

            return self.instruction

    def _configure_to_registers(self):
            self.instruction_type = 'R'
            self.rs = self.instruction[6:11]
            self.rt = self.instruction[11:16]
            self.rd = self.instruction[16:21]
            self.shamt = self.instruction[21:26]
            self.func = self.instruction[26:32]

            return self.instruction

    def has_offset(self):
        if self.instruction_type == 'R':
            return False

        return True

    def get_type(self):
        return self.instruction_type

    def get_function(self):
        return self.func

    def get_registers(self):
        registers = {
            'rs': self.rs,
            'rt': self.rt,
            'rd': self.rd
        }
        return registers

    def get_offset(self):
        if not self.has_offset():
            return None

        return extend_to_bits(self.offset)

    def get_func(self):
        if self.op != '000000':
            return FUNCTIONS[self.op]

        return FUNCTIONS[self.func]

    def __repr__(self):
        representation = "-" * 50
        representation += \
            "\nInstruction: {}\nType: {}\nOperation: {}\n".format(
                self.instruction,
                self.instruction_type,
                self.get_func()
            )

        representation += "-" * 50

        return representation


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
