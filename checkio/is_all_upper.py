def is_all_upper(text: str) -> bool:
    all_not_letter = True
    for letter in text.replace(" ",""):
        if letter.isalpha() and letter.isupper() == False:
            all_not_letter = False
            break
    return (text.replace(" ","").isupper() and text.replace(" ","").isalpha()) or  text.strip() == '' or all_not_letter

print('Example prn= ',is_all_upper("1S23"))


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
