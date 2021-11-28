#https://www.acmicpc.net/problem/1915

import sys

n, m = map(int, sys.stdin.readline().split())
mat = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if i>0 and j>0 and mat[i][j]==1:
            mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
        ans = max(ans, mat[i][j])

print(ans**2)
