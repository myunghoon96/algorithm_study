#https://www.acmicpc.net/problem/14716

import sys
from collections import deque

r,c=map(int,sys.stdin.readline().strip().split())

mat=[]
v = [[0] * c for _ in range(r)]

for i in range(r):
    temp=list(map(int,sys.stdin.readline().strip().split()))
    mat.append(temp)


def bfs(x,y):

    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        v[x][y] = 1

        if x-1>=0 and mat[x-1][y]==1 and v[x-1][y]==0:
            q.append((x-1,y))
            v[x-1][y]=1
        if y - 1 >= 0 and mat[x][y-1]==1 and v[x][y-1]==0:
            q.append((x,y-1))
            v[x][y - 1]= 1
        if x+1<r and mat[x+1][y]==1 and v[x+1][y]==0:
            q.append((x+1,y))
            v[x + 1][y]=1
        if y + 1<c and mat[x][y+1]==1 and v[x][y+1]==0:
            q.append((x,y+1))
            v[x][y + 1]=1
        #################################################
        if x-1>=0 and y-1>=0 and mat[x-1][y-1]==1 and v[x-1][y-1]==0:
            q.append((x-1,y-1))
            v[x-1][y-1]=1
        if y - 1 >= 0 and x+1<r and mat[x+1][y-1]==1 and v[x+1][y-1]==0:
            q.append((x+1,y-1))
            v[x+1][y - 1]= 1
        if x+1<r and y+1<c and mat[x+1][y+1]==1 and v[x+1][y+1]==0:
            q.append((x+1,y+1))
            v[x + 1][y+1]=1
        if y + 1<c and x-1>=0 and mat[x-1][y+1]==1 and v[x-1][y+1]==0:
            q.append((x-1,y+1))
            v[x-1][y + 1]=1


ans=0
for i in range(r):
    for j in range(c):
        if mat[i][j]==1 and v[i][j]==0:
            bfs(i,j)
            ans+=1

print(ans)
