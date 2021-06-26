#https://www.acmicpc.net/problem/14502

import sys
import copy

n,m = map(int,(input().split()))
mat=[[0]*m for _ in range(n)]
v=[]
for i in range(n):
    temp=list(map(int,(input().split())))
    for j in range(m):
        mat[i][j]=temp[j]
        if temp[j]==2:
            v.append((i,j))


ans=-1*sys.maxsize
def bfs():
    global ans
    mat2=copy.deepcopy(mat)
    v2=copy.deepcopy(v)
    while v2:
        x, y = v2.pop()

        dx=[0, 0, 1, -1]
        dy=[1, -1, 0, 0]

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<n and 0<=yy<m and mat2[xx][yy]==0:
                mat2[xx][yy]=2
                v2.append((xx,yy))

    temp=0
    for i in range(n):
        for j in range(m):
            if mat2[i][j]==0:
                temp+=1

    ans=max(ans,temp)


def setWall(cnt):
    if cnt==3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                mat[i][j]=1
                setWall(cnt+1)
                mat[i][j]=0


setWall(0)

print(ans)

