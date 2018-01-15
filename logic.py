from utils import extend_to_32, to_binary


class ALU:

    @sinalize
    def makeSum(self, a, b):
        negative = False

        result = int(a, 2) + int(b, 2)

        if result < 0:
            negative = True

        result = to_binary(abs(result))

        return extend_to_32(result, negative)

    @sinalize
    def makeSub(self, a, b):
        negative = False

        result = int(a, 2) - int(b, 2)

        if result < 0:
            negative = True

        result = to_binary(abs(result))

        return extend_to_32(result, negative)

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
