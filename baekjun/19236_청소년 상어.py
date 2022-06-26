# https://www.acmicpc.net/problem/19236

import sys

import copy

ans = -1
def fish_shark_move(shark_x, shark_y, shark_direc, shark_ate, matrix):
    global ans
    ans = max(ans, shark_ate)

    #fish_move
    for fish_no in range(1, 17):
        fish_x, fish_y, fish_direc = -1, -1, -1

        for i in range(4):
            for j in range(4):
                if matrix[i][j][0] == fish_no:
                    fish_x, fish_y, fish_direc = i, j, matrix[i][j][1]

        if fish_x == -1:
            continue

        for _ in range(8):
            xx = fish_x + dx[fish_direc]
            yy = fish_y + dy[fish_direc]

            if 0 <= xx < 4 and 0 <= yy < 4 and matrix[xx][yy][0] != -1:
                # another_fish
                if matrix[xx][yy][0] > 0:
                    another_fish_no = matrix[xx][yy][0]
                    another_fish_direc = matrix[xx][yy][1]
                    matrix[xx][yy] = [fish_no, fish_direc]
                    matrix[fish_x][fish_y] = [another_fish_no, another_fish_direc]

                # empty room
                elif matrix[xx][yy][0] == 0:
                    matrix[xx][yy] = [fish_no, fish_direc]
                    matrix[fish_x][fish_y] = [0, 0]    

                break

            fish_direc += 1
            fish_direc %= 8

    #shark_move
    for idx in range(1, 4):
        xx = shark_x + idx * dx[shark_direc]
        yy = shark_y + idx * dy[shark_direc] 

        if 0 <= xx < 4 and 0 <= yy < 4 and matrix[xx][yy][0] > 0:
            new_matrix = copy.deepcopy(matrix)
            eaten_fish_no = new_matrix[xx][yy][0]
            new_shark_direc = new_matrix[xx][yy][1]

            new_matrix[xx][yy] = [-1, 0] 
            new_shark_ate = shark_ate + eaten_fish_no
            new_matrix[shark_x][shark_y] = [0, 0]
            
            fish_shark_move(xx, yy, new_shark_direc, new_shark_ate, new_matrix)




dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#fish_no, fish_direction
matrix = [[[]]*4 for _ in range(4)]

for i in range(4):
    tmp_input = list(map(int, sys.stdin.readline().split()))
    for j in range(0,8,2):
        fish_no, fish_direc =tmp_input[j], tmp_input[j+1]
        matrix[i][int(j//2)] = [fish_no, fish_direc-1]

shark_x, shark_y = 0, 0 
eaten_fish_no, shark_direc = matrix[0][0]
shark_ate = eaten_fish_no
matrix[0][0][0] = -1

fish_shark_move(shark_x, shark_y, shark_direc, shark_ate, matrix)

print(ans)