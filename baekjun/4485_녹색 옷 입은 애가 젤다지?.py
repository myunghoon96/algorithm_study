# https://www.acmicpc.net/problem/4485
import sys
from collections import deque

question_idx = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    distances = [[int(1e9)] * N for _ in range(N)]

    def bfs():
        global question_idx 
        q = deque([(0, 0)])
        distances[0][0] = matrix[0][0]

        while q:
            x, y = q.popleft()
            dist = distances[x][y]

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if 0 <= xx < N and 0 <= yy < N:
                    if dist + matrix[xx][yy] < distances[xx][yy]:
                        distances[xx][yy] = dist + matrix[xx][yy]
                        q.append((xx, yy))

        print("Problem ", question_idx, ": ", distances[-1][-1], sep="")
        question_idx += 1

    bfs()
