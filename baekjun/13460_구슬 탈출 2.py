#https://www.acmicpc.net/problem/13460

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix=[]
visit=[[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

r_xy=(-1,-1)
b_xy=(-1,-1)
o_xy=(-1,-1)

for i in range(N):
    temp=list(sys.stdin.readline().strip())
    matrix.append(temp)
    for j in range(M):
        if temp[j]=="R":
            r_xy=(i,j)
        elif temp[j] =="B":
            b_xy=(i,j)
        elif temp[j] =="O":
            o_xy=(i,j)


dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    q=deque()
    cnt=0
    q.append((r_xy[0],r_xy[1],b_xy[0],b_xy[1],cnt))
    visit[r_xy[0]][r_xy[1]][b_xy[0]][b_xy[1]] = 1

    while q:
        if cnt+1>10:
            return -1

        rx,ry,bx,by,cnt=q.popleft()

        for index in range(4):
            xx=dx[index]
            yy=dy[index]

            nrx,nry,nbx,nby=rx,ry,bx,by

            rmove=0
            bmove=0
            r_status=0
            b_status=0

            while(1):
                nrx+=xx
                nry+=yy
                rmove+=1

                if matrix[nrx][nry]=='O':
                    r_status=1
                    break

                elif matrix[nrx][nry]=='#':
                    nrx-=xx
                    nry-=yy
                    break

            while(1):
                nbx+=xx
                nby+=yy
                bmove+=1

                if matrix[nbx][nby]=='O':
                    b_status=1
                    break

                elif matrix[nbx][nby]=='#':
                    nbx-=xx
                    nby-=yy
                    break


            if b_status==1:
                continue

            if r_status==1:
                return cnt+1

            if nrx==nbx and nry==nby:
                if rmove>bmove:
                    nrx-=xx
                    nry-=yy
                else:
                    nbx-=xx
                    nby-=yy

            if visit[nrx][nry][nbx][nby]==0:
                visit[nrx][nry][nbx][nby]=1
                q.append((nrx,nry,nbx,nby,cnt+1))
        
    return -1

print(bfs())
