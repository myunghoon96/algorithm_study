#https://www.acmicpc.net/problem/2636

import sys
from collections import deque

r, c= map(int, sys.stdin.readline().strip().split())
mat=[]


for i in range(r):
    temp=list(map(int,sys.stdin.readline().strip().split()))
    mat.append(temp)



cnt=0
cl=[]
def bfs(x,y):
    global cnt
    v=[[0]*c for _ in range(r)]
    q=deque()
    q.append((x,y))
    cnt=0

    while q:
        x,y=q.popleft()

        if x-1>=0 and mat[x-1][y]==0 and v[x-1][y]==0:
            q.append((x-1,y))
            v[x-1][y]=1
        if y - 1 >= 0 and mat[x][y-1] == 0 and v[x][y-1]==0:
            q.append((x,y-1))
            v[x][y - 1] = 1
        if x+1<r and mat[x+1][y] == 0 and v[x+1][y]==0:
            q.append((x+1,y))
            v[x + 1][y] =1
        if y + 1<c and mat[x][y+1] == 0 and v[x][y+1]==0:
            q.append((x,y+1))
            v[x][y + 1] =1

        if x-1>=0 and mat[x-1][y]==1 and v[x-1][y]==0:
            mat[x-1][y]=0
            v[x-1][y]=1
            cnt+=1
        if y - 1 >= 0 and mat[x][y-1] ==1 and v[x][y-1]==0:
            mat[x][y-1] =0
            v[x][y - 1] = 1
            cnt += 1
        if x+1<r and mat[x+1][y] == 1 and v[x+1][y]==0:
            mat[x+1][y] =0
            v[x + 1][y] =1
            cnt += 1
        if y + 1<c and mat[x][y+1] == 1 and v[x][y+1]==0:
            mat[x][y+1] =0
            v[x][y + 1] =1
            cnt += 1

ans=0
while 1:
    bfs(0,0)
    cl.append(cnt)
    if cnt==0:
        break
    ans+=1
print(ans)
print(cl[-2])
