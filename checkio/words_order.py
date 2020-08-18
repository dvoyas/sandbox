def words_order(text: str, words: list) -> bool:
    res = False
    i = 0
    word_s = set(words)
    for word in text.split():
        if i < len(words):
            res = False
            if word == words[i]:
                res = True
                i += 1
        else:
            break
    return res and i == len(words) and len(set(words)) == len(words)

if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world world im here', ['world', 'world']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
