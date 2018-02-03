from utils import (
    extend_to_bits, 
    to_binary, 
    to_integer,
    to_binaryC2,
    to_decimalC2
)


class ALU:

    def makeSum(self, a, b):

        result = to_decimalC2(a) + to_decimalC2(b)

        if result > (2**31 -1) or result < -(2**31):
            print("{}OVERFLOW OCURRENCE{}".format("-" * 20, "-" * 7))

        result = to_binaryC2(result)
        return result

    def makeSub(self, a, b):

        result = to_decimalC2(a) - to_decimalC2(b)

        if result > (2**31 -1) or result < -(2**31):
            print("{}OVERFLOW OCURRENCE".format("-" * 26))

        result = to_binaryC2(result)

        return result

    def makeAnd(self, a, b):

        a = int(a, 2)
        b = int(b, 2)

        result = to_binary((a & b))

        return extend_to_bits(result)

    def makeOr(self, a, b):

        a = int(a, 2)
        b = int(b, 2)

        result = to_binary((a | b))

        return extend_to_bits(result)
    
    def makeNot(self, a):
        a_len = len(a)

        a = to_decimalC2(a)

        result = to_binaryC2(~a, a_len)

        return result
