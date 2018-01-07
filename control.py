import abc


class BaseControl(abc.ABC):

    def __init__(self, cpu):
        self.cpu = cpu

    @abc.abstractmethod
    def execute(self):
        pass


class ControlAdd(BaseControl):

    def execute(self):
        print("Leio o registrador 1")
        print("Leio o registrador 2")
        print("Calculo o valor dos registradores na ULA")
        print("Retorno para o registrador de escrita setado na instruçao")
