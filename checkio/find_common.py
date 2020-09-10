def checkio(line1: str, line2: str) -> str:
    result = []
    for word in line1.split(','):
        if word in line2.split(','):
            result.append(word)
    result.sort()

    return ','.join(result)

# OTHER SOLUTION
#     s = [word for word in line1.split(',') if word in line2.split(',')]
#     s.sort()
#     return ','.join(s)


if __name__ == '__main__':
    print("Example:")
    print(checkio("mega,cloud,two,website,final","window,penguin,literature,network,fun,cloud,final,sausage"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")

