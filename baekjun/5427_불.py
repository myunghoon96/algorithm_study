# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    W, H = map(int, sys.stdin.readline().split())
    matrix = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

    fires = []
    people = []
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == '@':
                people.append((0,i,j))
            elif matrix[i][j] == '*':
                fires.append((0,i,j))
    

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque(fires)
    people_q = deque(people)

    time = 0
    ans_time = -1
    people_visit = [[False]*W for _ in range(H)]
    t, x, y = people[0]
    people_visit[x][y] = True

    while people_q:
        # escape success
        # print(time, people_q)
        if ans_time != -1:
            break

        while q and q[0][0] == time:
            t, x, y = q.popleft()

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if 0 <= xx < H and 0 <= yy < W and (matrix[xx][yy] != '*' and matrix[xx][yy] != '#'):
                    matrix[xx][yy] = '*'
                    q.append((t+1, xx, yy))

        while people_q and people_q[0][0] == time:
            
            t, x, y = people_q.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if 0 <= xx < H and 0 <= yy < W and matrix[xx][yy] == '.' and not people_visit[xx][yy]:
                    people_visit[xx][yy] = True
                    people_q.append((t+1, xx, yy))

                if xx < 0 or xx >= H or yy < 0 or yy >= W:
                    ans_time = time + 1
           
        time += 1

    if ans_time != -1:
        print(ans_time)
    else:
        print("IMPOSSIBLE")
    