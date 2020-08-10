from datetime import date

def days_diff(a, b):
    year1,month1,day1 = a
    year2,month2,day2 = b
    d1 = date(year1,month1,day1)
    d2 = date(year2,month2,day2)

    return abs(d1.toordinal() - d2.toordinal())


if __name__ == '__main__':
    print("Example:")
    print(days_diff([1,1,1],[9999,12,31]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff([1,1,1],[9999,12,31]) == 3652058
    print("Coding complete? Click 'Check' to earn cool rewards!")
