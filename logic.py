from utils import (
    extend_to_bits, 
    to_binary, 
    to_integer,
    to_binaryC2,
    to_decimalC2
)
# from decorators import sinalize


class ALU:

    # @sinalize
    def makeSum(self, a, b):

        result = to_decimalC2(a) + to_decimalC2(b)

        if result > (2**31 -1) or result < -(2**31):
            print("{}OVERFLOW OCURRENCE".format("-" * 26))

        result = to_binaryC2(result)
        return result

    # @sinalize
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
        
        a = int(a, 2)

        result = to_binarcyC2(~a)

        return result
