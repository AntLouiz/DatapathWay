def to_integer(binary_number):
    if not isinstance(binary_number, str):
        raise Exception()

    return int(binary_number, 2)


def to_binary(number):
    if not isinstance(number, int):
        raise Exception()

    return "{:0b}".format(number)


def extend_to_32(binary_number, negative=False):
    if not isinstance(binary_number, str):
        return None

    number_length = len(binary_number)

    if number_length < 0 or number_length > 32:
        raise Exception("The length of word is incorrect")

    result = 32 - number_length

    zero_fill = "0" * result

    if negative:
        zero_fill = "1{}".format(zero_fill[1:])

    return "{}{}".format(zero_fill, binary_number)


def binaryC2(number):
    if number >= 0:
        number = to_binary(number)
        number = extend_to_32(number)
    else:
        number = 2**32 + number
        number = to_binary(number)
        number = extend_to_32(number)

    return number

def decimalC2(binary):
    r = ['0']*32

    if binary == '11111111111111111111111111111111':
        return -1

    if binary[0] == '0':
        binary = int(binary, 2)
    else:
        for x in range(0,len(binary)):
            if (binary[x] == '0'):
                r[x] = '1'
            elif (binary[x] == '1'):
                r[x] ='0'
        binary = ''.join(r)

        result = bin(int(binary, 2) + int('1',2))

        binary = int(binary, 2) * -1

    return binary