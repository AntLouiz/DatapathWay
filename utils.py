def to_integer(binary_number):
    if not isinstance(binary_number, str):
        raise Exception()

    return int(binary_number, 2)


def to_binary(number):
    if not isinstance(number, int):
        raise Exception()

    return "{:0b}".format(number)


def extend_to_32(binary_number, negative=False):
    number_length = len(binary_number)

    if number_length < 0:
        raise Exception("The length of word is less than 0.")

    result = 32 - number_length

    zero_fill = "0" * result

    if negative:
        zero_fill = "1{}".format(zero_fill[1:])

    return "{}{}".format(zero_fill, binary_number)
