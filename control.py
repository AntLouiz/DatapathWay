import abc
from utils import to_integer, to_decimalC2


class BaseControl(abc.ABC):

    def __init__(self, cpu):
        self.cpu = cpu

    @abc.abstractmethod
    def execute(self):
        pass


class ControlAdd(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        print(instruction)

        rd = registers['rd']

        rs = registers['rs']
        print("Read the register 1: {}{}[{}]".format(rs, ' '*25, to_integer(rs)))

        rt = registers['rt']
        print("Read the register 2: {}{}[{}]".format(rt, ' '*25, to_integer(rt)))

        register_data1 = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data1, ))

        register_data2 = self.cpu.registers.get_value(rt)
        print("Read data 2: {}".format(register_data2, ))

        print("ALU-in-1:    {}{}[{}]".format(register_data1, ' '*6, to_decimalC2(register_data1)))
        print("ALU-in-2:    {}{}[{}]".format(register_data2, ' '*6, to_decimalC2(register_data2)))

        alu_result = self.cpu.alu.makeSum(register_data1, register_data2)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        self.cpu.registers.set_value(rd, alu_result)
        print("Write data:  {}".format(alu_result, ))
        
        print("Write register: {}{}[{}]".format(rd, ' '*30, to_integer(rd)))
        
        print("{}".format("-" * 64))
        print("\n\n")


class ControlSub(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        print(instruction)

        rd = registers['rd']

        rs = registers['rs']
        print("Read the register 1: {}{}[{}]".format(rs, ' '*25, to_integer(rs)))

        rt = registers['rt']
        print("Read the register 2: {}{}[{}]".format(rt, ' '*25, to_integer(rt)))

        register_data1 = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data1))

        register_data2 = self.cpu.registers.get_value(rt)
        print("Read data 2: {}".format(register_data2))

        print("ALU-in-1:    {}{}[{}]".format(register_data1, ' '*6, to_decimalC2(register_data1)))
        print("ALU-in-2:    {}{}[{}]".format(register_data2, ' '*6, to_decimalC2(register_data2)))

        alu_result = self.cpu.alu.makeSub(register_data1, register_data2)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        self.cpu.registers.set_value(rd, alu_result)
        print("Write data:  {}".format(alu_result))

        print("Write register: {}{}[{}]".format(rd, ' '*30, to_integer(rd)))
        
        print("{}".format("-" * 64))
        print("\n\n")   


class ControlAnd(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        print(instruction)

        rd = registers['rd']

        rs = registers['rs']
        print("Read the register 1: {}{}[{}]".format(rs, ' '*25, to_integer(rs)))

        rt = registers['rt']
        print("Read the register 2: {}{}[{}]".format(rt, ' '*25, to_integer(rt)))

        register_data1 = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data1))

        register_data2 = self.cpu.registers.get_value(rt)
        print("Read data 2: {}".format(register_data2))

        print("ALU-in-1:    {}{}[{}]".format(register_data1, ' '*6, to_decimalC2(register_data1)))
        print("ALU-in-2:    {}{}[{}]".format(register_data2, ' '*6, to_decimalC2(register_data2)))

        alu_result = self.cpu.alu.makeAnd(register_data1, register_data2)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        self.cpu.registers.set_value(rd, alu_result)
        print("Write data:  {}".format(alu_result))

        print("Write register: {}{}[{}]".format(rd, ' '*30, to_integer(rd)))
        
        print("{}".format("-" * 64))
        print("\n\n")


class ControlOr(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        print(instruction)

        rd = registers['rd']

        rs = registers['rs']
        print("Read the register 1: {}{}[{}]".format(rs, ' '*25, to_integer(rs)))

        rt = registers['rt']
        print("Read the register 2: {}{}[{}]".format(rt, ' '*25, to_integer(rt)))

        register_data1 = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data1))

        register_data2 = self.cpu.registers.get_value(rt)
        print("Read data 2: {}".format(register_data2))

        print("ALU-in-1:    {}{}[{}]".format(register_data1, ' '*6, to_decimalC2(register_data1)))
        print("ALU-in-2:    {}{}[{}]".format(register_data2, ' '*6, to_decimalC2(register_data2)))

        alu_result = self.cpu.alu.makeOr(register_data1, register_data2)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        self.cpu.registers.set_value(rd, alu_result)
        print("Write data:  {}".format(alu_result))

        print("Write register: {}{}[{}]".format(rd, ' '*30, to_integer(rd)))
        
        print("{}".format("-" * 64))
        print("\n\n")


class ControlLw(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        offset = instruction.get_offset()
        print(instruction)

        rt = registers['rt']
        rs = registers['rs']
        print("Read the register 1:{}{}{}[{}]".format(' '*20, rs, ' '*6, to_integer(rs)))

        register_data = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data))

        print("ALU-in-1:    {}{}[{}]".format(register_data, ' '*6, to_decimalC2(register_data)))
        print("ALU-in-2:    {}{}[{}]".format(offset, ' '*6, to_decimalC2(offset)))

        alu_result = self.cpu.alu.makeSum(register_data, offset)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        print("Address:     {}".format(alu_result))

        memory_data = self.cpu.memory.get_value(alu_result)
        print("Read data:   {}".format(memory_data))

        self.cpu.registers.set_value(rt, memory_data)
        print("Write data:  {}{}[{}]".format(memory_data, ' '*6, to_decimalC2(memory_data)))
        print("Write register:{}{}{}[{}]".format(' '*25, rt, ' '*6, to_integer(rt)))
        
        print("{}".format("-" * 64))
        print("\n\n")


class ControlSw(BaseControl):

    def execute(self):
        instruction = self.cpu.pc.next_instruction
        registers = instruction.get_registers()
        offset = instruction.get_offset()
        print(instruction)

        rs = registers['rs']
        print("Read the register 1:{}{}{}[{}]".format(' '*20, rs, ' '*6, to_integer(rs)))

        rt = registers['rt']
        print("Read the register 2:{}{}{}[{}]".format(' '*20, rt, ' '*6, to_integer(rt)))

        register_data1 = self.cpu.registers.get_value(rs)
        print("Read data 1: {}".format(register_data1))

        register_data2 = self.cpu.registers.get_value(rt)
        print("Read data 2: {}".format(register_data2))

        print("ALU-in-1:    {}{}[{}]".format(register_data1, ' '*6, to_decimalC2(register_data1)))
        print("ALU-in-2:    {}{}[{}]".format(offset, ' '*6, to_decimalC2(offset)))

        alu_result = self.cpu.alu.makeSum(register_data1, offset)
        print("ALU-result:  {}{}[{}]".format(alu_result, ' '*6, to_decimalC2(alu_result)))

        print("Address:     {}".format(alu_result))

        self.cpu.memory.set_value(alu_result, register_data2)
        print("Write data:  {}{}[{}]".format(register_data2, ' '*6, to_decimalC2(register_data2)))
        
        print("{}".format("-" * 64))
        print("\n\n")
