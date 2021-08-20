#https://www.acmicpc.net/problem/2178
row, col = map(int, (input().split()))

matrix=[[0]*col for i in range(row)]


for i in range(row):
    temp=input()
    for j in range(col):
        matrix[i][j]=int(temp[j])



def bfs(x,y):

    if x==row-1 and y==col-1:
        return

    while(queue):
        x, y =queue.pop(0)
        dx=[1, -1, 0, 0]
        dy=[0, 0, 1, -1]

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<row and 0<=yy<col and matrix[xx][yy]==1:
                queue.append((xx, yy))
                matrix[xx][yy]=matrix[x][y]+1

queue=[(0,0)]
bfs(0,0)

print(matrix[row-1][col-1])