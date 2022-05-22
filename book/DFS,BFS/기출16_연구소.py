#https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

viruses = deque()
zeros = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            viruses.append((i,j))
        elif matrix[i][j] == 0:
            zeros.append((i,j))

zero_combis = combinations(zeros, 3)


dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = -1

def bfs(vrs, mat):
    global ans

    visit = [[0]*m for _ in range(n)]
    for e in vrs:
        x, y = e
        visit[x][y] = 1

    while vrs:
        x, y = vrs.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and visit[xx][yy] == 0 and mat[xx][yy] == 0:
                visit[xx][yy] = 1
                mat[xx][yy] = 2
                vrs.append((xx,yy))

    safe_area = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                safe_area += 1
    ans = max(ans, safe_area)

for zero_combi in zero_combis:

    tmp_mat = copy.deepcopy(matrix)
    tmp_viruses = copy.deepcopy(viruses)
    for xy_pair in zero_combi:
        x, y = xy_pair
        tmp_mat[x][y] = 1
    bfs(tmp_viruses, tmp_mat)


print(ans)