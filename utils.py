def to_integer(binary_number):
    if not isinstance(binary_number, str):
        raise Exception()

    return int(binary_number, 2)


def to_binary(number):
    if not isinstance(number, int):
        raise Exception()

    return "{:0b}".format(number)


def extend_16_to_32(binary_number):
    number_length = len(binary_number)

    if number_length < 16:
        raise Exception("The length of word is less than 16.")

    result = 32 - number_length

    zero_fill = "0" * result

    return "{}{}".format(zero_fill, binary_number)
