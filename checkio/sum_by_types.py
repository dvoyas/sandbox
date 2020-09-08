from typing import Tuple

def sum_by_types(items: list) -> Tuple[str, int]:
    # your code here
    s = ''
    i = 0
    for item in items:
        if type(item) == str:
            s += item
        else:
            i += item
    return (s, i)

# THE BEST RESULT
#     result = ['', 0]
#     for item in items:
#         result[isinstance(item, int)] += item
#     return result


# OTHER SOLUTION
#     accum = {T: T() for T in (str, int)}
#     for elem in a: accum[type(elem)] += elem
#     return tuple(accum.values())


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2', 3]) == ('12', 3)
    assert sum_by_types(['1', '2', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
