#https://www.acmicpc.net/problem/2638

import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0,]

def outside_air():
    out_visit = [[0]*m for _ in range(n)]
    q=deque([(0,0)])
    out_visit[0][0]=1
    mat[0][0]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<n and 0<=yy<m and out_visit[xx][yy]==0 and mat[xx][yy]!=1:
                out_visit[xx][yy]=1
                mat[xx][yy]=2
                q.append((xx,yy))


def melt(x,y):
    outside = 0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and mat[xx][yy]==2:
            outside+=1
    if outside>=2:
        return True
    return False

def check_zero():
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:    
                return False            
    return True

time = 0

while True:
    if check_zero()==True:
        break

    outside_air()
    melt_set = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:                            
                if melt(i,j):
                    melt_set.add((i,j))
                    
    for ij in melt_set:
        i,j=ij
        mat[i][j]=0

    time+=1

print(time)