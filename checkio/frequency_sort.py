def frequency_sort(items_):
    dict = {}
    # print(set(items_))
    for item in set(items_):
        dict[item] = items_.count(item)
    # new_dict ={}
    # for i in sorted(dict.values()):
    #     print(i, dict[i], end = " ")

    new_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    print(new_dict)
    res = []
    # for i in sorted
    for key,value in new_dict.items():
        # print(key,value)
        res += [key]*value
    return res


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    # frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
