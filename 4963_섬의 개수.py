#https://www.acmicpc.net/problem/4963

import sys
from collections import deque

while(1):
    w,h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    matrix=[]
    visit=[[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        temp=list(map(int, sys.stdin.readline().split()))
        matrix.append(temp)

    def bfs(i,j):
        q=deque()
        q.append((i,j))
        visit[i][j]=1

        while q:
            x,y = q.popleft()

            dx=[1,-1,0,0,1,1,-1,-1]
            dy=[0,0,1,-1,1,-1,1,-1]
            for i in range(8):
                xx=x+dx[i]
                yy=y+dy[i]

                if 0<=xx<h and 0<=yy<w and visit[xx][yy]==0 and matrix[xx][yy]==1:
                    visit[xx][yy]=1
                    q.append((xx,yy))


    ans=0
    for i in range(h):
        for j in range(w):
            if visit[i][j]==0 and matrix[i][j]==1:
                bfs(i,j)
                ans+=1

    print(ans)
