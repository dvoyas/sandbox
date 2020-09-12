def follow(instructions):
    res =[0,0]
    for inst in instructions:
        if inst == 'r':
            res[0] = res[0] + 1
        elif inst == 'l':
            res[0] = res[0] - 1
        elif inst == 'f':
            res[1] = res[1] + 1
        elif inst == 'b':
            res[1] = res[1] - 1
    return (res[0], res[1])

# OTHER SOLUTION
#     rules = {"f": [1, 0], 'b': [-1, 0], 'l': [0, -1], 'r': [0, 1]}
#
#     x = 0
#     y = 0
#     for c in list(instructions):
#         r = rules[c]
#
#         x = x + r[1]
#         y = y + r[0]
#
#     return (x, y)

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
