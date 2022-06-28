# https://www.acmicpc.net/problem/19237

import sys, copy
from collections import defaultdict

def minus_smell():
    for i in range(N):
        for j in range(N):
            if matrix[i][j][1] == 1:
                matrix[i][j] = [0, 0]
            elif matrix[i][j][1] > 1:
                matrix[i][j][1] -= 1

def check_other_shark():
    for i in range(N):
        for j in range(N):
            if matrix[i][j][0] > 1 and matrix[i][j][1] == K:
                return True
    return False

dic = defaultdict(list)
N, M, K = map(int, sys.stdin.readline().split())
matrix = [[[0,0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp_input = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if tmp_input[j] > 0:
            matrix[i][j][0] = tmp_input[j]
            matrix[i][j][1] = K
shark_directions = [-1] + list(map(int, sys.stdin.readline().split()))
for i in range(1, M+1):
    dic[i].append(list(map(int, sys.stdin.readline().split())))
    dic[i].append(list(map(int, sys.stdin.readline().split())))
    dic[i].append(list(map(int, sys.stdin.readline().split())))
    dic[i].append(list(map(int, sys.stdin.readline().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
    if not check_other_shark() or time >= 1001:
        break
    new_matrix = copy.deepcopy(matrix)

    # find no smell
    for i in range(N):
        for j in range(N):
            if matrix[i][j][0] > 0 and matrix[i][j][1] == K and matrix[i][j] == new_matrix[i][j]:
                cur_direction = shark_directions[matrix[i][j][0]] - 1
                cur_shark = matrix[i][j][0]
                priority_directions = dic[cur_shark][cur_direction]
                no_smell_areas = []
                self_smell_areas = []

                for priority_direction in priority_directions:
                    xx = i + dx[priority_direction-1]
                    yy = j + dy[priority_direction-1]
                    if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] == [0, 0]:
                        no_smell_areas.append((xx, yy, priority_direction))
                        shark_directions[cur_shark] = priority_direction

                        if new_matrix[xx][yy][0] == 0:
                            new_matrix[xx][yy][0] = cur_shark
                            new_matrix[xx][yy][1] = K + 1
                            
                        else:
                            new_matrix[xx][yy][0] = min(new_matrix[xx][yy][0], cur_shark)
                        
                        break
                    # change direction to self smell, and go to self smell
                    elif 0 <= xx < N and 0 <= yy < N and matrix[xx][yy][0] == cur_shark:
                        self_smell_areas.append((xx, yy, priority_direction))

                if not no_smell_areas:
                    xx, yy, priority_direction = self_smell_areas[0]
                    shark_directions[cur_shark] = priority_direction

                    new_matrix[xx][yy][0] = cur_shark
                    new_matrix[xx][yy][1] = K + 1

    matrix = new_matrix

    minus_smell()

    time += 1

if time >= 1001:
    print(-1)
else:
    print(time)