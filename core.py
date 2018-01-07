from memory import RegistersBank, Memory
from logic import ALU
from instructions import PC
from control import (
    ControlSw,
    ControlLw,
    ControlAdd,
    ControlSub,
    ControlAnd,
    ControlOr,
)


class CPU:
    def __init__(self):
        self.alu = ALU()
        self.pc = PC()
        self.registers = RegistersBank()
        self.memory = Memory()
        self.control_types = {
            'add': ControlAdd(self),
            'sub': ControlSub(self),
            'and': ControlAnd(self),
            'or': ControlOr(self),
            'lw': ControlLw(self),
            'sw': ControlSw(self)
        }

    def execute(self):
        for instruction in self.pc.get_instructions():
            instruction_func = instruction.get_func()

            print(instruction)
            self.control_types[instruction_func].execute()
