#https://www.acmicpc.net/problem/2468

import sys
from collections import deque
N=int(sys.stdin.readline())
matrix=[]
minNum=101
maxNum=-1

for i in range(N):
    temp=list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)
    if minNum>min(temp):
        minNum=min(temp)
    if maxNum<max(temp):
        maxNum=max(temp)    


def bfs(i,j,h,visit):

    q=deque()
    q.append((i,j))
    visit[i][j]=1

    while q:
        x,y=q.popleft()
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]

        for index in range(4):
            xx=x+dx[index]
            yy=y+dy[index]

            if 0<=xx<N and 0<=yy<N and visit[xx][yy]==0 and matrix[xx][yy]>h:
                q.append((xx,yy))
                visit[xx][yy]=1

ansList=[]
for h in range(minNum, maxNum+1):
    visit=[[0 for _ in range(N)] for _ in range(N)]
    ans=0
    for i in range(N):
        for j in range(N): 
            if visit[i][j]==0 and matrix[i][j]>h:
                bfs(i,j,h,visit)                       
                ans+=1
    ansList.append(ans)

if max(ansList)==0:
    print(1)
else:
    print(max(ansList))
