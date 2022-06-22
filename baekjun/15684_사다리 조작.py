# https://www.acmicpc.net/problem/15684

import sys
import copy

N, M, H = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1

def check():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H+1):
            if matrix[j][now - 1] == 1:
                now -= 1       
            elif matrix[j][now] == 1:
                now += 1
                
            if j == H:
                if now != i:
                    return False
    return True

candidates = []
for i in range(1, H + 1) :
    for j in range(1, N) :
        if matrix[i][j-1] == 0 and matrix[i][j] == 0 and matrix[i][j+1] == 0 :
            candidates.append([i, j])

def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(candidates)):
        x, y = candidates[c]
        if not matrix[x][y-1] and not matrix[x][y+1]:
            matrix[x][y] = True
            dfs(depth+1, c+1)
            matrix[x][y] = False

# answer = int(1e9)
# dfs(0, 0)

# if answer == int(1e9):
#     print(-1)
# else:
#     print(answer)
answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)