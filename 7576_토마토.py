#https://www.acmicpc.net/problem/7576
from collections import deque

col, row = map(int, (input().split()))

matrix=[[0]*col for i in range(row)]


for i in range(row):
    temp=input().split(' ')
    for j in range(col):
        matrix[i][j]=int(temp[j])


def bfs():

    while(queue):

        x, y =queue.popleft()
        dx=[1, -1, 0, 0]
        dy=[0, 0, 1, -1]

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<row and 0<=yy<col and matrix[xx][yy]==0:
                queue.append((xx, yy))
                matrix[xx][yy]=matrix[x][y]+1


queue=deque()

for i in range(row):
    for j in range(col):
        if matrix[i][j]==1:
            queue.append((i,j))


bfs()
ans=0
status=1
for i in range(row):
    for j in range(col):
        ans=max(ans,matrix[i][j])
        if matrix[i][j]==0:
            status=0


# for i in range(row):
#     print(matrix[i])

if status:
    print(ans-1)
else:
    print(-1)

