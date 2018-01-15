def sinalize(func):
    def sinalize_wrapper(obj, *args):
        binary_nums = list()

        for binary_num in args:
            binary_num = list(binary_num)
            if binary_num[0] == '1':
                binary_num[0] = '-'

            binary_num = ''.join(binary_num)
            binary_nums.append(binary_num)

        return func(obj, *binary_nums)

    return sinalize_wrapper
