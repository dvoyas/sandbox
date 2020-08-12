def split_pairs(a):
    word = ''
    res = []
    for char in a:
        word += char
        if len(word) == 2:
            res.append(word)
            word = ''
    if word != '':
        res.append(word + '_')
    return res


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
