from typing import List

def checkio(matrix: List[List[int]]) -> bool:
    # print(len(matrix[0]))
    # for l in range(len(matrix))
    len_ = len(matrix)
    for i in range(0,len_):
        count_h = 1
        count_v = 1
        count_r = 1
        # for j in range(0,len_-1):
        #     if matrix[i][j] == matrix[i][j+1]:
        #         count_h += 1
        #     else:
        #         count_h = 1
        #     if count_h > 3:
        #         return True
        # for j in range(0,len_-1):
        #     if matrix[j][i] == matrix[j+1][i]:
        #         count_v += 1
        #     else:
        #         count_v = 1
        #     if count_v > 3:
        #         return True
        for j in range(0,len_-1):
            if matrix[i + j][j] == matrix[i + j+1][j+1]:
                # print('j j', matrix[j][j])
                count_r += 1
            else:
                # print('j j', matrix[j][j])
                count_r = 1
            if count_r > 3:
                return True
            if matrix[j][i+j] == matrix[j+1][i+j+1]:
                # print('j j', matrix[j][j])
                count_r += 1
            else:
                # print('j j', matrix[j][j])
                count_r = 1
            if count_r > 3:
                return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [2, 1, 1, 1],
        [1, 1, 3, 1],
        [1, 3, 1, 6],
        # [1, 7, 2, 5]
        [3, 3, 3, 3]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 1, 3, 2],
        [1, 1, 9, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
