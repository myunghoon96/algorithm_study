# https://www.acmicpc.net/problem/3184

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i, j, visit):
    q = deque()
    q.append((i,j))
    tmp_sheep = [(i,j)]
    tmp_wolf = []

    while q:
        x, y = q.popleft()
        # print("x y", (x, y))
        for idx in range(4):
            xx = x + dx[idx]
            yy = y + dy[idx]
            # print("xx yy", (xx, yy))
            if 0 <= xx < R and 0 <= yy < C and matrix[xx][yy] != '#' and (xx, yy) not in visit:
                visit.add((xx, yy))
                q.append((xx, yy))
                if matrix[xx][yy] == 'o':
                    tmp_sheep.append((xx, yy))
                elif matrix[xx][yy] == 'v':
                    tmp_wolf.append((xx, yy))

    # print((i,j), tmp_sheep, tmp_wolf)
    if len(tmp_sheep) > len(tmp_wolf):
        for x, y in tmp_wolf:
            matrix[x][y] = '.'
    else:
        for x, y in tmp_sheep:
            matrix[x][y] = '.'

visit = set()
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'o' and (i, j) not in visit:
            visit.add((i,j))
            bfs(i, j, visit)

sheep_cnt, wolf_cnt = 0, 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'o':
            sheep_cnt += 1
        elif matrix[i][j] == 'v':
            wolf_cnt += 1
print(sheep_cnt, wolf_cnt)