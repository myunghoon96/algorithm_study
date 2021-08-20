#https://www.acmicpc.net/problem/16234

import sys
from collections import deque

n,l,r=map(int,sys.stdin.readline().strip().split())

mat=[]


for i in range(n):
    temp=list(map(int,sys.stdin.readline().strip().split()))
    mat.append(temp)


def bfs(x,y):

    q=deque()
    q.append((x,y))

    cl=[]


    while q:
        x,y=q.popleft()

        v[x][y] = 1
        cl.append((x,y))
        val=mat[x][y]

        if x-1>=0 and l<=abs(val-mat[x-1][y])<=r and v[x-1][y]==0:
            q.append((x-1,y))
            v[x-1][y]=1
        if y - 1 >= 0 and l<=abs(val-mat[x][y-1])<=r and v[x][y-1]==0:
            q.append((x,y-1))
            v[x][y - 1]= 1
        if x+1<n and l<=abs(val-mat[x+1][y])<=r and v[x+1][y]==0:
            q.append((x+1,y))
            v[x + 1][y]=1
        if y + 1<n and l<=abs(val-mat[x][y+1])<=r and v[x][y+1]==0:
            q.append((x,y+1))
            v[x][y + 1]=1

    if len(cl)>1:
        temp=0
        for e in cl:
            x=e[0]
            y=e[1]
            temp+=mat[x][y]

        avg=temp//len(cl)
        for e in cl:
            x=e[0]
            y=e[1]
            mat[x][y]=avg

    return len(cl)

ans=0

flag=1
while 1:
    v = [[0] * n for _ in range(n)]
    if flag==0:
        break
    flag=0

    for i in range(n):
        for j in range(n):
            if v[i][j]==0:
                v[i][j]=1
                if bfs(i,j)>1:
                    flag=1

    if flag:
        ans+=1

print(ans)

