# https://www.acmicpc.net/problem/6593

import sys
from collections import deque

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break

    matrix = [[] for _ in range(L)]

    for k in range(L):
        for _ in range(R):
            matrix[k].append(list(sys.stdin.readline().rstrip()))
        sys.stdin.readline().rstrip()

    for k in range(L):
        for i in range(R):
            for j in range(C):
                if matrix[k][i][j] == 'S':
                    start = (k, i, j)
                elif matrix[k][i][j] == 'E':
                    end = (k, i, j)

    moves = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    q = deque()
    q.append((0, start[0], start[1], start[2]))
    visit = set()
    visit.add((start[0], start[1], start[2]))
    ans_time = -1
    while q:
        time, z, x, y = q.popleft()
        # print('time, z, x, y', time, z, x, y)
        if (z, x, y) == end:
            ans_time = time
            break

        for move in moves:
            zz = z + move[0]
            xx = x + move[1]
            yy = y + move[2]

            if 0 <= zz < L and 0 <= xx < R and 0 <= yy < C and (zz, xx, yy) not in visit and matrix[zz][xx][yy] != '#':
                visit.add((zz, xx, yy))
                q.append((time + 1, zz, xx, yy))

    if ans_time != -1:
        print("Escaped in", time ,"minute(s).")
    else:

        print("Trapped!")
