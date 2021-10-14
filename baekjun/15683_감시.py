#https://www.acmicpc.net/problem/15683

import sys
import copy

n,m = map(int, sys.stdin.readline().split())
matrix = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

cctv_position = []
for i in range(n):
    for j in range(m):
        if 1<=matrix[i][j]<=5:
            cctv_position.append((matrix[i][j],i,j))
cctv_count = len(cctv_position)

def cctv_dir(cctv):
    #north, east, south, west
    if cctv == 1:
        dir = [[0],[1],[2],[3]]
    elif cctv == 2:
        dir = [[0,2],[1,3]]    
    elif cctv == 3:
        dir = [[0,1],[1,2],[2,3],[3,0]]    
    elif cctv == 4:
        dir = [[3,0,1], [0,1,2], [1,2,3], [2,3,0]]
    elif cctv == 5:
        dir = [[0,1,2,3]]

    return dir

def watch(d, x, y, mat):
    mat[x][y]=7
    xx = dx[d]+x
    yy = dy[d]+y
    
    while 0<=xx<n and 0<=yy<m:
        if mat[xx][yy] == 6:
            break
        
        if mat[xx][yy] != 6:
            mat[xx][yy]=7
        
        xx += dx[d]
        yy += dy[d]

    return mat

def count(mat):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                cnt += 1
    return cnt

ans = 100
def dfs(idx, mat):
    global ans
    if idx == len(cctv_position):
        cnt = count(mat)
        ans = min(ans, cnt)
        return

    cctv_type, x, y = cctv_position[idx]

    dirs = cctv_dir(cctv_type)
    for dir in dirs:
        temp_mat = copy.deepcopy(mat)
        for d in dir:
            temp_mat = watch(d,x,y,temp_mat)
 
        dfs(idx+1, temp_mat)

dfs(0, matrix)
print(ans)