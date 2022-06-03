# https://www.acmicpc.net/problem/2239
import sys

matrix = [[0]*9 for _ in range(9)]
zeros = []
for i in range(9):
    row = sys.stdin.readline().rstrip()
    for j in range(9):
        matrix[i][j] = int(row[j])
        if matrix[i][j] == 0:
            zeros.append((i,j))


def possible(x,y,num,mat):
    #row
    for i in range(9):
        if num == mat[x][i]:
            return False

    #col
    for i in range(9):
        if num == mat[i][y]:
            return False

    #square
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if num == mat[i][j]:
                return False
    
    return True


def dfs(mat, cnt):
    if cnt == len(zeros):
        for e in mat:
            print(*e, sep='')
        exit()

    zero = zeros[cnt]
    x, y = zero
    for candidate in range(1, 10):
        if possible(x, y, candidate, mat):
            mat[x][y] = candidate
            dfs(mat, cnt + 1)
        mat[x][y] = 0

dfs(matrix, 0)