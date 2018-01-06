import abc


class BaseMemory:
    data = {}

    def set_value(self, address, value):
        """
        Set a value with a given address
        """

        self.data[address] = value

        return True

    @abc.abstractmethod
    def get_value(self, address):
        """
        Return a value with a given address
        """

        return self.data[address]
