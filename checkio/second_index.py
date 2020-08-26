def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here text.find(symbol) + text[text.find(symbol):].find(symbol)
    if text.find(symbol) == -1:
        pass
    elif text[text.find(symbol) + 1:].find(symbol) == -1:
        pass
    else:
        return text.find(symbol) + 1 + text[text.find(symbol)+1:].find(symbol)


if __name__ == '__main__':
    print('Example:')
    print(second_index("hi", " "))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
