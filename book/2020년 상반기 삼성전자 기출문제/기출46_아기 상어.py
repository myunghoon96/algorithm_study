# https://www.acmicpc.net/problem/16236
from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
fishes = []

shark_x, shark_y = 0, 0
shark_size = 2
shark_eat = 0

for i in range(N):
    for j in range(N):
        if 1 <= matrix[i][j] <=6:
            fishes.append((i, j, matrix[i][j]))
        elif matrix[i][j] == 9:
            shark_x, shark_y = i, j
            matrix[i][j] = 0
def bfs():
    global shark_x, shark_y, shark_size, fishes, shark_eat
    # print('fishes ', fishes, 'shark_size',shark_size)
    smaller_fishes = []
    for fish in fishes:
        fish_x, fish_y, fish_size = fish
        if fish_size < shark_size:
            smaller_fishes.append((fish_x, fish_y))
    
    if len(smaller_fishes) == 0:
        return
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([(shark_x, shark_y, shark_size, 0)])
    visit = set()
    visit.add((shark_x, shark_y))
    eat_fishes = []
    while q:
        x, y, sz, dist = q.popleft()
        if (x, y) in smaller_fishes and sz > matrix[x][y]:
            eat_fishes.append((dist, x, y))
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N and (xx,yy) not in visit and sz >= matrix[xx][yy]:
                visit.add((xx,yy))
                q.append((xx, yy, shark_size, dist + 1))

   
    eat_fishes.sort(key = lambda x : (x[0],x[1],x[2]))
    #there is smaller fish, but can not access, thus len(eat_fishes) == 0
    #     3
    # 0 0 0
    # 0 0 3
    # 9 3 1
    if len(eat_fishes) <= 0:
        return
    c_dist, c_x, c_y = eat_fishes[0]
    fishes.remove((c_x, c_y, matrix[c_x][c_y]))

    matrix[c_x][c_y] = 0
    shark_eat += 1
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0
    shark_x = c_x
    shark_y = c_y

    return c_dist

ttl_time = 0
while True:
    result = bfs()
    if result == None:
        print(ttl_time)
        break
    else:
        ttl_time += result