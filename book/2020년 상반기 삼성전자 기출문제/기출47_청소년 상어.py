# https://www.acmicpc.net/problem/19236
from collections import defaultdict
matrix = [[0]*(4) for _ in range(4)]
fishes = []

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        # fish_NO, fish_direction
        matrix[i][j] = (info[j*2], info[j*2+1])

for e in matrix:
    print(e)

shark_x, shark_y = 0, 0
matrix[shark_x][shark_y] = (-1, matrix[0][0][1])
directions = [i for i in range(1, 8)]
moves = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0), 6:(1,1), 7:(0,1), 8:(-1,1) }

def move_fish():
    fishes = defaultdict()

    for i in range(4):
        for j in range(4):
            if 1 <= matrix[i][j][0] <= 16:
                fish_no, fish_direc = matrix[i][j]
                fishes[fish_no] = [i, j, fish_direc]

    print('sorted(fishes.keys())', sorted(fishes.keys()))
    for fish_no in sorted(fishes.keys()):
        fish_x, fish_y, fish_direc = fishes[fish_no]
        # if fish_no > 1:
        #     print('fish_no > 1 break')
        #     break
        print('fish_no', fish_no)
        for _ in range(8):
            xx = fish_x + moves[fish_direc][0]
            yy = fish_y + moves[fish_direc][1]
            print('xx yy', xx, yy)
            if 0 <= xx < 4 and 0 <= yy < 4 and (xx != shark_x and yy != shark_y):
                if matrix[xx][yy][0] > 0 : # there is another fish
                    another_fish_no = matrix[xx][yy][0]
                    another_fish_x, another_fish_y, another_fish_direc = fishes[another_fish_no]

                    fishes[another_fish_no] = [fish_x, fish_y, another_fish_direc]
                    fishes[fish_no] = [another_fish_x, another_fish_y, fish_direc]

                    matrix[fish_x][fish_y] = (another_fish_no, fish_direc)
                    matrix[another_fish_x][another_fish_y] = (fish_no, another_fish_direc)
                    # matrix[fish_x][fish_y], matrix[xx][yy] = matrix[xx][yy], matrix[fish_x][fish_y]
                    break
            else:
                fish_direc += 1
                if fish_direc == 9:
                    fish_direc = 1
move_fish()
for e in matrix:
    print(e)