def to_integer(binary_number):
    if not isinstance(binary_number, str):
        raise Exception()

    return int(binary_number, 2)


def to_binary(number):
    if not isinstance(number, int):
        raise Exception()

    return "{:0b}".format(number)


def extend_to_bits(binary_number, bits = 32):
    if not isinstance(binary_number, str):
        return None

    number_length = len(binary_number)

    result = bits - number_length

    zero_fill = "0" * result

    return "{}{}".format(zero_fill, binary_number)


def to_binaryC2(number, bits = 32):
    if not isinstance(number, int):
        raise Exception()

    if number >= 0 :
        number = to_binary(number)
        number = extend_to_bits(number, bits)
        return number
    else:
        number = 2**bits + number
        number = to_binary(number)
        number = extend_to_bits(number, bits)
        return number


def to_decimalC2(binary_number):
    if not isinstance(binary_number, str):
        return None 

    bits = len(binary_number)

    decimal = int(binary_number, 2)

    if binary_number[0] == '0':
        return decimal       
    else:
        decimal = - (2**bits -1) + decimal -1
        return decimal