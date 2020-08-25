from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    i = len(items)
    if i == 0 or i == 1:
        return True
    i -= 1
    res = False
    while i > 0:
        if items[i] > items[i-1]:
            res = True
            i -= 1
        else:
            return False

    return res

# OTHER SOLUTIONS
#     return all(items[x]>items[x-1]for x in range(1,len(items)))

# THE BEST SOLUTION
#     return all(items[i] < items[i+1] for i in range(len(items)-1))


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([4, 5, 6, 7, 3, 7, 9]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
