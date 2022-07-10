# acmicpc.net/problem/10830

import sys, copy

N, B = map(int, sys.stdin.readline().split())
original_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def get_row(idx, matrix):
    return matrix[idx]

def get_col(idx, matrix):
    col = []
    for i in range(N):
        col.append(matrix[i][idx])
    return col

def cal(row, col):
    tmp_sum = 0
    for i in range(N):
        tmp_sum += (row[i] * col[i])
    return tmp_sum

def calculate(mat1, mat2):
    mat3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat3[i][j] += cal(get_row(i, mat1), get_col(j, mat2))
            mat3[i][j] %= 1000
    return mat3

def divide(mat, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] %= 1000
        return mat
    
    tmp_mat = divide(mat, b//2)
    if b % 2 == 0:
        return calculate(tmp_mat, tmp_mat)
    elif b % 2 != 0:
        return calculate(calculate(tmp_mat, tmp_mat), mat)

ans = divide(original_matrix, B)

for e in ans:
    print(*e)