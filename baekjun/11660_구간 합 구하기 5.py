# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

prefix = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        prefix[i+1][j+1] = matrix[i][j] 

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] += prefix[i][j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] += prefix[i-1][j]

# print()
# for e in prefix:
#     print(e)

infos = [list(map(int, input().split())) for _ in range(M)]

for info in infos:
    x1, y1, x2, y2 = info
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])


# prefix[4][5] =  prefix[2][5] + prefix[4][2]-prefix[2][2] + d

# 3,3 -> 4, 5

# d =[4][5] - [2][5] - [4][2] + [2][2]

# x2y2 - (x1-1)y2 - x1(y1-1) + (x1-1)(y1-1)

# 1 2 3 4