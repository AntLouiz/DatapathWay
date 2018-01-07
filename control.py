import abc
from utils import to_binary


class BaseControl(abc.ABC):

    def __init__(self, cpu):
        self.cpu = cpu

    @abc.abstractmethod
    def execute(self):
        pass


class ControlAdd(BaseControl):

    def execute(self):
        print("Read the register 1")
        print("Read the register 2")
        print("Sum the registers values on the ALU")
        print("Return the result to the write register")


class ControlSub(BaseControl):

    def execute(self):
        print("Read the register 1")
        print("Read the register 2")
        print("Sub the registers values on the ALU")
        print("Return the result to the write register")


class ControlAnd(BaseControl):

    def execute(self):
        print("Read the register 1")
        print("Read the register 2")
        print("Make a AND with the registers values on the ALU")
        print("Return the result to the write register")


class ControlOr(BaseControl):

    def execute(self):
        print("Read the register 1")
        print("Read the register 2")
        print("Make a OR with the registers values on the ALU")
        print("Return the result to the write register")


class ControlLw(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        offset = instruction.offset
        rt = registers['rt']
        rs = registers['rs']
        print("Read register 1: {}".format(rs))

        register_data = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data))

        print("ALU-in-1: {}".format(register_data))
        print("ALU-in-2: {}".format(offset))

        alu_result = self.cpu.alu.makeSum(register_data, offset)
        print("ALU-result: {}".format(alu_result))

        print("Address: {}".format(alu_result))

        alu_result = to_binary(int(alu_result, 2))
        memory_data = self.cpu.memory.get_value(alu_result)
        print("Read data: {}".format(memory_data))

        self.cpu.registers.set_value(rt, memory_data)
        print("Write data: {}".format(memory_data))
        print("Write register: {}".format(rt))

class ControlSw(BaseControl):

    def execute(self):
        print("Read the register 1")
        print("Read the register 2")
        print("Sum the offset with the value of the register 1 in ALU")
        print("Write the data of register 2 on the ALU result address")
