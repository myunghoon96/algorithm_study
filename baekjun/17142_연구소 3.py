# https://www.acmicpc.net/problem/17142

import sys
from itertools import combinations
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
viruses = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            viruses.append((i,j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans_time = int(1e9)

def bfs(mat, vrs):
    global ans_time

    q = deque()
    for a, b in vrs:
        q.append((a, b, 10))   
        mat[a][b] = 10 

    zero_cnt = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                zero_cnt += 1

    while q:
        x, y, time = q.popleft()

        if zero_cnt == 0:
            break

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
        
            if 0 <= xx < N and 0 <= yy < N and (mat[xx][yy] == 0 or mat[xx][yy] == 2):
                q.append((xx, yy, time + 1))
                if mat[xx][yy] == 0:
                    zero_cnt -= 1
                mat[xx][yy] = time + 1


    # print(vrs, zero_cnt)
    # for e in mat:
    #     print(e)
    # print()

    if zero_cnt == 0:
        
        max_time = -1
        for i in range(N):
            for j in range(N):
                max_time = max(max_time, mat[i][j])

        max_time -= 10
        ans_time = min(ans_time, max_time)
        # print("YAS", max_time)

combis = combinations(viruses, M)
for combi in combis:
    mat = copy.deepcopy(matrix)
    bfs(mat, combi)

if ans_time == int(1e9):
    print(-1)
else:
    print(ans_time)