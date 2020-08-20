# Your optional code here
# You can import some modules or create additional functions


def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # replace this for solution
    data_new = []
    for i in range(len(data)):
        data_new.append(data[i]) if data[i] in data[:i] + data[i+1:] else None
    return data_new

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list

#  THE BEST SOLUTION
    #return [i for i in data if data.count(i) > 1]



if __name__ == "__main__":
    # checkio([1, 2, 3, 1, 3])
    print(checkio([1, 2, 3, 1, 3]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
