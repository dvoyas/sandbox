# # Taken from mission Acceptable Password V
#
# # Taken from mission Acceptable Password IV
#
# # Taken from mission Acceptable Password III
#
# # Taken from mission Acceptable Password II
#
# # Taken from mission Acceptable Password I
#
# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return len(password) > 6
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
#
# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return len(password) > 6 and any(char.isdigit() for char in password)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == False
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() == False
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == False
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return (len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() == False) or len(password) > 9
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('short54') == True
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     assert is_acceptable_password('12345678910') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
#
# def is_acceptable_password(a):
#     return ((len(a) > 6 and any(char.isdigit() for char in a) and a.isdigit() == False) or len(a) > 9) and 'PASSWORD' not in a.upper()
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('short54') == True
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     assert is_acceptable_password('muchlonger5') == True
#     assert is_acceptable_password('sh5') == False
#     assert is_acceptable_password('1234567') == False
#     assert is_acceptable_password('12345678910') == True
#     assert is_acceptable_password('password12345') == False
#     assert is_acceptable_password('PASSWORD12345') == False
#     assert is_acceptable_password('pass1234word') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

def is_acceptable_password(a):
    # your code here
    return (((len(a) > 6 and any(char.isdigit() for char in a) and a.isdigit() == False) or len(a) > 9) and 'PASSWORD' not in a.upper()) and len(set(a)) > 2


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('aaaaaabbbbb'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
