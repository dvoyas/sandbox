def split_pairs(a):
    # word = ''
    # res = []
    # for char in a:
    #     word += char
    #     if len(word) == 2:
    #         res.append(word)
    #         word = ''
    # if word != '':
    #     res.append(word + '_')
    # return res

    # return [ch1 for ch1 in zip(a[::2])]
    # return [ch1 + ch2 for ch1, ch2 in zip(a[::2], a[1::2] + '_')]
    # return a[::2]#
    return  zip(a[::2], a[1::2] + '_')


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(split_pairs('abcd')) == ['ab', 'cd']
    # assert list(split_pairs('abc')) == ['ab', 'c_']
    # assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    # assert list(split_pairs('a')) == ['a_']
    # assert list(split_pairs('')) == []
    # print("Coding complete? Click 'Check' to earn cool rewards!")
