def to_integer(binary_number):
    if not isinstance(binary_number, str):
        raise Exception()

    return int(binary_number, 2)


def to_binary(number):
    if not isinstance(number, int):
        raise Exception()

    return "{:0b}".format(number)
