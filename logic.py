from utils import (
    extend_to_32, 
    to_binary, 
    binaryC2,
    decimalC2
)
from decorators import sinalize


class ALU:

    @sinalize
    def makeSum(self, a, b):
        negative = False

        result = decimalC2(a) + decimalC2(b)

        if result > 2147483647 or result < -2147483648:
            print("{}OVERFLOW OCURRENCE".format("-" * 26))

        result = binaryC2(result)
        return result

    @sinalize
    def makeSub(self, a, b):
        negative = False

        result = decimalC2(a) - decimalC2(b)

        if result > 2147483647 or result < -2147483648:
            print("{}OVERFLOW OCURRENCE".format("-" * 26))

        result = binaryC2(result)

        return result

    def makeAnd(self, a, b):

        a = int(a, 2)
        b = int(b, 2)

        result = to_binary((a & b))

        return extend_to_32(result)

    def makeOr(self, a, b):
        a = int(a, 2)
        b = int(b, 2)

        result = to_binary((a | b))

        return extend_to_32(result)
