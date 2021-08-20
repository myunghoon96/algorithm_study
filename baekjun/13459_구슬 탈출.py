#https://www.acmicpc.net/problem/13459

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix=[]
visit=[[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

r_xy=(-1,-1)
b_xy=(-1,-1)
o_xy=(-1,-1)



def mov(rx,ry, bx, by, xx, yy):
    rx2=rx
    ry2=ry
    bx2=bx
    by2=by
    status=0
    r_status=0
    b_status=0
    rmove=0
    bmove=0
    while(1):

        rx+=xx
        ry+=yy
        rmove+=1

        if matrix[rx][ry]=='O':
            r_status=1
            break

        elif matrix[rx][ry]=='#':
            rx-=xx
            ry-=yy
            break

    while(1):

        bx+=xx
        by+=yy
        bmove+=1

        if matrix[bx][by]=='O':
            b_status=1
            break

        elif matrix[bx][by]=='#':
            bx-=xx
            by-=yy
            break

    if b_status==1:
        return rx2,ry2,bx2,by2,0

    if r_status==1 and b_status==0:
        status=1

    if rx==bx and ry==by:
        if rmove>bmove:
            rx-=xx
            ry-=yy
        else:
            bx-=xx
            by-=yy

    return rx,ry,bx,by,status

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


ans=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs():
    q=deque()
    cnt=0

    q.append((r_xy[0],r_xy[1],b_xy[0],b_xy[1],cnt))
    visit[r_xy[0]][r_xy[1]][b_xy[0]][b_xy[1]] = 1

    while q:
        if cnt+1>10:
            return 0

        rx,ry,bx,by,cnt=q.popleft()

        for index in range(4):
            rx2,ry2,bx2,by2,status=mov(rx,ry,bx,by,dx[index],dy[index])
            if status==1:
                return 1

            if visit[rx2][ry2][bx2][by2]==0:
                visit[rx2][ry2][bx2][by2]=1
                q.append((rx2,ry2,bx2,by2,cnt+1))
        
    return 0

print(bfs())
