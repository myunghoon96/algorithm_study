#https://www.acmicpc.net/problem/3190
from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
time_direcs = [list(input().split()) for _ in range(L)]

snake = deque([(0,0)])
# 북 동  남 서
directions = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur_direc = 1

def move(snake, direc):
    new_head_x, new_head_y = snake[-1][0] + dx[direc], snake[-1][1] + dy[direc]
    # print(new_head_x, new_head_y)
    if (new_head_x, new_head_y) in snake or new_head_x >= N or new_head_x < 0 or new_head_y >=N or new_head_y < 0:
        return False
    
    snake.append((new_head_x, new_head_y))
    # print((new_head_x+1, new_head_y+1), apples)
    if [new_head_x+1, new_head_y+1] in apples:
        # print("EAT APPLE")
        apples.remove([new_head_x+1, new_head_y+1])
    else:
        snake.popleft()  

    return True
time = 0
time_idx = 0

while True:

    # print('cur_direc, ', cur_direc)
    if time_idx < L:
        change_time, change_direc = time_direcs[time_idx]
        if int(change_time) == time:
            if change_direc == 'D':
                cur_direc += 1
                cur_direc %= 4
            elif change_direc == 'L':
                cur_direc -= 1
                cur_direc %= 4
            time_idx += 1


    # print('time ' , time,  'snake ', snake, 'cur_direc ', cur_direc)
    if move(snake, cur_direc) == False:
        # print("MOVE FALSE BREAK", time)
        print(time+1)
        break
    time += 1