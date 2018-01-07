import abc


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
