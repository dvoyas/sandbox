def goes_after(word: str, first: str, second: str) -> bool:

    return first in word[word.find(first):word.find(first)+1] and second in word[word.find(first)+1:word.find(first)+2] and word!='' and word.find(first) != len(word)-1 and word.find(first) < word.find(second)

# OTHER SOLUTION
# return first+second in word and word.index(first)+1 == word.index(second)

# THE BEST SOLUTION
#     try:
#         return word.index(second)-word.index(first) == 1
#     except ValueError:
#         return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('almaz', 'r', 'a'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('word', 'w', 'o') == True
    assert goes_after('almaz', 'r', 'a') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
