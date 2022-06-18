# https://www.acmicpc.net/problem/4179

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

people = []
fires = []
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'J':
            people.append((0, i, j))
        elif matrix[i][j] == 'F':
            fires.append((0, i, j))

people_q = deque(people)
fires_q = deque(fires)
people_visit = set()
people_visit.add((people[0][1], people[0][2]))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans_time = -1
time = 0
while people_q and ans_time == -1:
    # print(time, people_q, fires_q)

    while fires_q and fires_q[0][0] == time and ans_time == -1:
        t, x, y = fires_q.popleft()
        # print('fire', t, x, y)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < R and 0 <= yy < C and matrix[xx][yy] != '#':
                fires_q.append((t + 1, xx, yy))
                matrix[xx][yy] = '#'

    while people_q and people_q[0][0] == time and ans_time == -1:
        t, x, y = people_q.popleft()
        # print('people', t, x, y)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < R and 0 <= yy < C and (xx, yy) not in people_visit and matrix[xx][yy] == '.':
                people_visit.add((xx,yy))
                people_q.append((t + 1, xx, yy))
            elif xx < 0 or xx >= R or yy < 0 or yy >= C:
                ans_time = t + 1
                break
    
    time += 1


if ans_time == -1:
    print("IMPOSSIBLE")
else:
    print(ans_time)