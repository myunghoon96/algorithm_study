#https://www.acmicpc.net/problem/3190
import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = [tuple(map(int,sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
directions = [list(sys.stdin.readline().split()) for _ in range(l)]
# print(apples)
# print(directions)
d = [0, 1, 2 ,3] #north, east, south, west
move = [[-1,0], [0,1], [1,0], [0,-1]]
cur_d = 1
cur_head = (1,1)
snake = deque()
snake.append((1,1))

def change_direction(cur_direction, turn):
    if turn == 'L':
        cur_direction-=1
        cur_direction%=4
    elif turn == 'D':
        cur_direction+=1
        cur_direction%=4

    return cur_direction

directions_idx=0
time = 1
while True:
    
    cur_head = snake[-1]
    next_head = (cur_head[0]+move[cur_d][0], cur_head[1]+move[cur_d][1])
    # print("step ", time, cur_head, next_head, snake)
    if next_head in snake:
        # print("snake meets it self")
        break
    if next_head[0]<=0 or next_head[0]>n or next_head[1]<=0 or next_head[1]>n:
        # print("snake meets the wall", next_head, cur_head)
        break

    snake.append(next_head)

    if next_head in apples:
        # print("eat apple ", next_head, apples)
        apples.remove(next_head)
        # print("remain apples", apples)
    else:
        snake.popleft()

    if directions_idx<len(directions):
        if time == int(directions[directions_idx][0]):
            befor_d = cur_d
            cur_d = change_direction(cur_d, directions[directions_idx][1])
            # print("IT is time to change direc", time, befor_d, cur_d)
            directions_idx+=1
    time+=1


# print(snake)
print(time)