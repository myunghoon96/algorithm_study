#https://www.acmicpc.net/problem/7569

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

matrix=[]

for _ in range(H):
    temp2=[]
    for _ in range(N):
        temp=list(map(int, sys.stdin.readline().split()))
        temp2.append(temp)
    matrix.append(temp2)


#matrix[H][N][M], visit[H][N][M]

visit=[[[0 for _ in range(M)]for _ in range(N)]for _ in range(H) ]

def bfs():
    q=deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if matrix[h][n][m]==1:
                    q.append((h,n,m))
                    visit[h][n][m]=1

    dx=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]
    while q:
        z,y,x=q.popleft()
        for index in range(6):
            xx=x+dx[index]
            yy=y+dy[index]
            zz=z+dz[index]

            if 0<=xx<M and 0<=yy<N and 0<=zz<H and visit[zz][yy][xx]==0 and matrix[zz][yy][xx]==0:
                q.append((zz,yy,xx))
                matrix[zz][yy][xx]=matrix[z][y][x]+1
                visit[zz][yy][xx]=1

bfs()
not_ripe_status=0
maxNum=-1
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m]==0:
                not_ripe_status=1
            maxNum=max(maxNum,matrix[h][n][m])   
            
if not_ripe_status==1:
    print(-1)
else:
    print(maxNum-1)
