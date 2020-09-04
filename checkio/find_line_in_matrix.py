from typing import List

def checkio(matrix: List[List[int]]) -> bool:
    len_ = len(matrix)
    for i in range(0,len_):
        count_h = 1
        count_v = 1
        for j in range(0,len_-1):
            if matrix[i][j] == matrix[i][j+1]:
                count_h += 1
            else:
                count_h = 1
            if count_h > 3:
                return True
        for j in range(0,len_-1):
            if matrix[j][i] == matrix[j+1][i]:
                count_v += 1
            else:
                count_v = 1
            if count_v > 3:
                return True

    matrix1 = []
    matrix2 = []
    for matr in matrix:
        matrix1 += matr
    for matr in matrix:
        matrix2 += matr[::-1]
    for matrix_ in [matrix1,matrix2]:
        for i in range(0,int(len(matrix_))-5):
            tmp = matrix_[i::len(matrix)+1]
            count_u = 1
            for j in range(0, len(tmp)-1):
                if tmp[j] == tmp[j+1]:
                    count_u += 1
                else:
                    count_u = 1
                if count_u > 3:
                    return True

    return False

#THE BEST SOLUTION
    N = len(matrix)
    def seq_len(x, y, dx, dy, num):
        if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
            return 1 + seq_len(x + dx, y + dy, dx, dy, num)
        else:
            return 0

    DIR = [(dx, dy) for dy in range(-1, 2)
                    for dx in range(-1, 2)
                    if dx != 0 or dy != 0]
    for y in range(N):
        for x in range(N):
            for dx, dy in DIR:
                if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
                    return True
    return False

# OTHER SOLUTION
# def check(numbers):
#     num = numbers[0]
#     len = 1
#     for n in numbers[1:]:
#         if num == n:
#             len += 1
#             if len >= 4:
#                 return True
#         else:
#             len = 1
#             num = n
#     return False
#
#
# def checkio(matrix):
#     # replace this for solution
#     width = len(matrix)
#     for n in range(width):
#         if check(matrix[n]):
#             return True
#         if check([matrix[m][n] for m in range(width)]):
#             return True
#         if check([matrix[n + m][m] for m in range(width - n)]):
#             return True
#         if check([matrix[m][n + m] for m in range(width - n)]):
#             return True
#         if check([matrix[n + m][width - m - 1] for m in range(width - n)]):
#             return True
#         if check([matrix[m][width - n - m - 1] for m in range(width - n)]):
#             return True
#     return False





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
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
        [5, 5, 5, 5, 5],
        [1, 1, 9, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 3, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
