def backward_string_by_word(text: str) -> str:
    result = []
    first = True
    for word in text.split(' '):
        if word == ' ':
            result += word
        else:
            # if first:
            #     result += word[::-1]
            #     first = False
            # else:
            #     result += ' '+ word[::-1]
            result.append(word[::-1])

    return " ".join(result)

    # words=text.split(" ")
    # rev=[]
    # for word in words:
    #     rev.append(word[::-1])
    # print("count= ", count)
    # return " ".join(rev)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(' world'))
    # print(backward_string_by_word('hello   world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello  world') == 'olleh  dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
