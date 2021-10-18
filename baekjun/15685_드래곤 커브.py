#https://www.acmicpc.net/problem/15685
import sys
n = int(sys.stdin.readline())
mat = [[0]*101 for _ in range(101)]

dy=[0,-1,0,1]
dx=[1,0,-1,0]

for _ in range(n):
    x,y,d,g = map(int, sys.stdin.readline().split())
    dirs = [d]
    mat[x][y]=1
    for _ in range(g):
        for d in dirs[::-1]:
            dirs.append((d + 1) % 4)

    for d in dirs:
        x+=dx[d]
        y+=dy[d]
        mat[x][y]=1

ans = 0
for i in range(100):
    for j in range(100):
        if mat[i][j]==1 and mat[i+1][j+1]==1 and mat[i+1][j]==1 and mat[i][j+1]==1:
            ans+=1
print(ans)
