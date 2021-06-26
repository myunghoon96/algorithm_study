#https://www.acmicpc.net/problem/1987

import sys


r,c=map(int,sys.stdin.readline().split())
mat=[]
for i in range(r):
    temp=sys.stdin.readline()
    mat.append(temp)

ans=0
def bfs():
    global ans
    q=set()
    q.add((0,0,mat[0][0]))


    while q:
        x, y, v = q.pop()
        dx=[0, 0, 1, -1]
        dy=[1, -1, 0, 0]
        ans=max(len(v),ans)

        if ans == 26:
            return ans

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<r and 0<=yy<c and mat[xx][yy] not in v:
                q.add((xx,yy, v+mat[xx][yy]))

    return ans

print(bfs())

