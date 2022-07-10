# https://www.acmicpc.net/problem/6087
import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
start_end_list = []

for i in range(H):
    for j in range(W):
        if matrix[i][j] == 'C':
            start_end_list.append((i, j))

start, end = start_end_list[0], start_end_list[1]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = int(1e9)
visit = [[[-1]*4 for _ in range(W)] for _ in range(H)]

def bfs():
    global ans
    q = deque()
    q.append((start[0], start[1], 0, 0))
    q.append((start[0], start[1], 1, 0))
    q.append((start[0], start[1], 2, 0))
    q.append((start[0], start[1], 3, 0))

    while q:
        x, y, direc, mirror_cnt = q.popleft()

        if (x, y) == end:
            ans = min(ans, mirror_cnt)
            visit[x][y][direc] = ans
            continue

        if visit[x][y][direc] == -1:
            visit[x][y][direc] = mirror_cnt

        else:
            if mirror_cnt < visit[x][y][direc]:
                visit[x][y][direc] = mirror_cnt 
            else:
                continue

        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]

            if 0 <= xx < H and 0 <= yy < W and matrix[xx][yy] != '*':
                if d == direc:
                    q.append((xx, yy, d, mirror_cnt))
                else:
                    q.append((xx, yy, d, mirror_cnt + 1))


bfs()

print(ans)