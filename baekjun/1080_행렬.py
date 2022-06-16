# https://www.acmicpc.net/problem/1080

import sys

N, M = map(int, sys.stdin.readline().split())

matrix1 = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
matrix2 = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def process(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if matrix1[i][j] == 0:
                matrix1[i][j] = 1
            elif matrix1[i][j] == 1:
                matrix1[i][j] = 0

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if matrix1[i][j] != matrix2[i][j]:
            process(i, j)
            ans += 1

for i in range(N):
    for j in range(M):
        if matrix1[i][j] != matrix2[i][j]:
            ans = -1

print(ans)