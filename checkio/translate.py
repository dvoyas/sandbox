VOWELS = "aeiouy"

def translate(phrase):
    skip = 1
    res_word = ''

    for char in phrase:
        skip -= 1
        if skip == 0:
            res_word += char
            if char == ' ':
                skip = 1
            elif char in VOWELS:
                skip = 3
            else:
                skip = 2

        # res += res_word if res == '' else ' ' + res_word


    return res_word

# OTHER SOLUTION
#     for i in VOWELS:
#         if 3*i in phrase:
#             phrase = phrase.replace(3*i, 2*i)
#     return ' '.join( [ i[::2] for i in phrase.split() ] )


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
