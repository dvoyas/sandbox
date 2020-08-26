def popular_words(text: str, words: list) -> dict:
    # result = {}
    # for i in range(0, len(words)):
    #     result[words[i]] = text.lower().split().count(words[i])

        lower_count = text.lower().split().count
        return {word: lower_count(word) for word in words}

    #all(countw.append(text.lower().split().count(words[x])) for x in range(1, len(words)))

    # return result


# THE BEST SOLUTION
#     lower_count = text.lower().split().count
#     return {word: lower_count(word) for word in words}


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
