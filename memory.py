from utils import to_binary


class BaseMemory:
    data = {}

    def set_value(self, address, value):
        """
        Set a value with a given address
        """

        self.data[address] = value

        return True

    def get_value(self, address):
        """
        Return a value with a given address
        """

        return self.data[address]


class RegistersBank(BaseMemory):
    def __init__(self):
        self.total_registers = 2**3

        for i in range(self.total_registers):
            binary_number = to_binary(i)
            self.data[binary_number] = False


class Memory(BaseMemory):
    pass
