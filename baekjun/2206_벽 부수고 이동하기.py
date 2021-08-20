#https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,(input().split(' ')))

matrix=[[0]*m for j in range(n)]
visit=[[[-1,-1] for _ in range(m)] for j in range(n)]
queue=deque()

for i in range(n):
    temp=input().strip()
    for j in range(m):
        matrix[i][j]=int(temp[j])

def f(x,y, cnt, br):

    queue.append([0,0,0,0])
    visit[x][y][br]=1

    while queue:
        temp=queue.popleft()
        x=temp[0]
        y=temp[1]
        cnt=temp[2]
        br=temp[3]

        if x == n - 1 and y == m - 1:
            print(cnt + 1)
            return

        if x+1<=n-1 and visit[x+1][y][br]==-1:
            visit[x+1][y][br]=1
            if matrix[x+1][y]==0:
                queue.append([x+1, y, cnt+1, br])
            elif matrix[x+1][y]==1 and br==0:
                queue.append([x+1, y, cnt+1, br+1])

        if x-1>=0 and visit[x-1][y][br]==-1:
            visit[x-1][y][br]=1
            if matrix[x-1][y]==0:
                queue.append([x-1, y, cnt+1, br])
            elif matrix[x-1][y]==1 and br==0:
                queue.append([x-1, y, cnt+1, br+1])

        if y+1<=m-1 and visit[x][y+1][br]==-1:
            visit[x][y+1][br]=1
            if matrix[x][y+1]==0:
                queue.append([x, y+1, cnt+1, br])
            elif matrix[x][y+1]==1 and br==0:
                queue.append([x, y+1, cnt+1, br+1])

        if y-1>=0 and visit[x][y-1][br]==-1:
            visit[x][y-1][br]=1
            if matrix[x][y-1]==0:
                queue.append([x, y-1, cnt+1, br])
            elif matrix[x][y-1]==1 and br==0:
                queue.append([x, y-1, cnt+1, br+1])

    print(-1)

f(0,0,0,0)

