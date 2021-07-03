#https://www.acmicpc.net/problem/2583

import sys
from collections import deque


N, M, Q = map(int, sys.stdin.readline().split())
matrix=[[0 for _ in range(M)] for _ in range(N) ]
for _ in range(Q):
    x1,y1,x2,y2=map(int, sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):

            matrix[i][j]=1

visit=[[0 for _ in range(M)] for _ in range(N) ]

def bfs(i,j):

    q=deque()
    q.append((i,j))
    visit[i][j]=1
    area=1

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        
        for index in range(4):
            xx=x+dx[index]
            yy=y+dy[index]

            if 0<=xx<N and 0<=yy<M and visit[xx][yy]==0 and matrix[xx][yy]==0:
                q.append((xx,yy))
                visit[xx][yy]=1
                area+=1

    return area

areaList=[]
cnt=0
for i in range(N):
    for j in range(M):
        if visit[i][j]==0 and matrix[i][j]==0:
            areaList.append(bfs(i,j))
            cnt+=1

areaList.sort()
print(cnt)
print(*areaList)

    
