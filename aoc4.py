import math
import numpy as np

def parse_matrix(f):
    matrix = []
    for i in range(5):
        line = f.readline().strip().split()
        line = [int(n) for n in line]
        matrix.append(line)

    return matrix

def check_for_win(bool_matrix):
    for row in range(len(bool_matrix)):
        if all(bool_matrix[row]):
            return True

    for col in range(len(bool_matrix[0])):
        column = [bool_matrix[row,col] for row in range(len(bool_matrix))]
        if all(column):
            return True

    return False

def find_num(matrix, num):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row,col] == num:
                return (row, col)
    return None

best_score = -1
matrices = []

with open('input4', 'r') as f:
    nums = f.readline().strip().split(",")
    nums = [int(n) for n in nums]

    while f.readline() != '':
        matrix = np.array(parse_matrix(f))
        matrices.append(matrix)
        bool_matrix = np.array([[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))])
        for i,n in enumerate(nums):
            loc = find_num(matrix, n)
            if loc is not None:
                bool_matrix[loc[0],loc[1]] = True
                print(f'{i} found {loc} == {n}')
            if check_for_win(bool_matrix):
                if best_score < i + 1:
                    best_score = i+1
                    best_matrix = matrix
                    best_bool_matrix = bool_matrix
                    last_num = n
                break


print(best_score)
bm = np.array(best_matrix)
bbm = np.array(best_bool_matrix)

cumsum = 0
for row in range(len(bm)):
    for col in range(len(bm[0])):
        if not bbm[row,col]:
            cumsum += bm[row,col]

