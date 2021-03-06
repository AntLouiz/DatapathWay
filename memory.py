import random
from utils import to_binary, extend_to_bits, to_binaryC2


class BaseMemory:

    def __init__(self):
        self.data = {}

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
    data = {}

    def __new__(cls, *args, **kwargs):
        """
        Make the BaseMemory a Monostate class
        """
        obj = super(RegistersBank, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.data

        return obj

    def __init__(self):
        total_registers = 2**5

        for i in range(total_registers):
            binary_number = to_binary(i)
            if len(binary_number) < 5:
                zero_fill = 5 - len(binary_number)
                binary_number = "{}{}".format(
                    "0" * zero_fill,
                    binary_number
                )

            if i == 8:
                self.data[binary_number] = extend_to_bits(to_binary(16))
            else:
                self.data[binary_number] = False


class Memory(BaseMemory):
    data = {}

    def __new__(cls, *args, **kwargs):
        """
        Make the BaseMemory a Monostate class
        """
        obj = super(Memory, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.data

        return obj

    def __init__(self):
        total_data = 2**8

        for i in range(total_data):
            binary_number = to_binary(i)
            binary_number = extend_to_bits(to_binary(i))

            random_number = to_binaryC2(
                random.randint(-(2**31), (2**31) - 1)
            )
            self.data[binary_number] = random_number

