# https://www.acmicpc.net/problem/16954
import sys
from collections import deque

start = (7, 0)
end = (0, 7)

matrix = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
walls = set()
for i in range(8):
    for j in range(8):
        if matrix[i][j] == '#':
            walls.add((i, j))

# 0, 0
dx = [0, 0, 1, -1, -1, -1, 1, 1, 0]
dy = [1, -1, 0, 0, -1, 1, -1, 1, 0]
def bfs():
    visit = set()
    q = deque()
    q.append((start[0],start[1]))

    #visit.add((start[0],start[1]))
    global walls

    while q:

        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) in walls:
                continue

            if (x, y) == end:
                return 1

            for i in range(9):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < 8 and 0 <= yy < 8 and (xx, yy) not in walls and (xx, yy) not in visit:
                    visit.add((xx, yy))
                    q.append((xx, yy))
                    
        new_walls = set()
        if len(walls) > 0:
            visit = set()

        for x, y in walls:
            if x + 1 < 8:
                new_walls.add((x+1, y))

        walls = new_walls
    return 0

print(bfs())
