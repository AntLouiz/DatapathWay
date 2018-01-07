import abc


class BaseControl(abc.ABC):

    def __init__(self, cpu):
        self.cpu = cpu

    @abc.abstractmethod
    def execute(self):
        pass
