# https://www.acmicpc.net/problem/1743

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
matrix = [[0]*M for _ in range(N)]
visit = [[False]*M for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x-1][y-1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans_size = -1
def bfs(i, j):
    global ans_size
    q = deque([(i, j)])
    visit[i][j] = True
    tmp_size = 1

    while q:
        x, y = q.popleft()
    
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy <M and matrix[xx][yy] == 1 and not visit[xx][yy]:
                visit[xx][yy] = True
                q.append((xx, yy))
                tmp_size += 1

    ans_size = max(tmp_size, ans_size)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visit[i][j]:
            bfs(i,j)

print(ans_size)