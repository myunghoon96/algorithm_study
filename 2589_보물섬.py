#https://www.acmicpc.net/problem/2589

import sys
from collections import deque

r, c= map(int, sys.stdin.readline().strip().split())
mat=[]


for i in range(r):
    temp=sys.stdin.readline().strip()
    mat.append(temp)

ans = -1 * sys.maxsize
# cl=[]
def bfs(x,y):
    global ans
    v=[[0]*c for _ in range(r)]
    q=deque()
    q.append((x,y))
    v[x][y]=1
    while q:
        x,y=q.popleft()
        if x-1>=0 and mat[x-1][y]=='L' and v[x-1][y]==0:
            q.append((x-1,y))
            v[x-1][y]=v[x][y]+1
        if y - 1 >= 0 and mat[x][y-1] == 'L' and v[x][y-1]==0:
            q.append((x,y-1))
            v[x][y - 1] = v[x][y]+1
        if x+1<r and mat[x+1][y] == 'L' and v[x+1][y]==0:
            q.append((x+1,y))
            v[x + 1][y] =v[x][y]+1
        if y + 1<c and mat[x][y+1] == 'L' and v[x][y+1]==0:
            q.append((x,y+1))
            v[x][y + 1] =v[x][y]+1


    for i in range(r):
        for j in range(c):
            ans=max(ans,v[i][j])

    # cl.append(ans)



for i in range(r):
    for j in range(c):
        if mat[i][j]=='L':
            bfs(i,j)

print(ans-1)
# print(cl)
