# https://www.acmicpc.net/problem/21610

import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ops = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx2 = [1,1,-1,-1]
dy2 = [1,-1,1,-1]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for op in ops:
    d, s = op
    # print()
    # print("op ", op)
    #1
    new_clouds = []
    for idx, cloud in enumerate(clouds):
        x, y = cloud
        xx = x + s * dx[d-1]
        yy = y + s * dy[d-1]
        
        xx %= N
        yy %= N
        new_clouds.append((xx, yy))
    
    # print('new_clouds', new_clouds)
    #2
    for new_cloud in new_clouds:
        x, y =  new_cloud
        matrix[x][y] += 1
    
    #3
    clouds = []
    # new_clouds = []

    #4
    for new_cloud in new_clouds:
        x, y = new_cloud
        has_water = 0
        for i in range(4):
            xx = x + dx2[i]
            yy = y + dy2[i]
            if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] >= 1:
                has_water += 1
        matrix[x][y] += has_water
    
    #5
    clouds = []
    for i in range(N):
        for j in range(N):
            if  matrix[i][j] >=2 and (i,j) not in new_clouds:
                matrix[i][j] -= 2
                clouds.append((i,j))


    # for e in matrix:
    #     print(e)
    
ans = 0
for i in range(N):
    for j in range(N):
        ans += matrix[i][j]
print(ans)
    
