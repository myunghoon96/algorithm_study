#https://www.acmicpc.net/problem/3055

from collections import deque
r, c= map(int, input().split())
mat=[['']*c for _ in range(r)]

sq=deque()
wq=deque()

for i in range(r):
    temp=input()
    for j in range(c):
        mat[i][j]=temp[j]
        if temp[j]=='S':
            start=(i,j)
            mat[i][j]=0
            sq.append(start)
        elif temp[j]=='*':
            w=(i,j)
            wq.append(w)

def bfs():

    while sq:

        for i in range(len(wq)):
            x, y = wq.popleft()

            if x-1>=0 and mat[x-1][y]=='.':
                mat[x-1][y]='*'
                wq.append([x-1,y])
            if y - 1 >= 0 and mat[x][y-1] == '.':
                mat[x][y-1]='*'
                wq.append([x,y-1])
            if x+1<r and mat[x+1][y] == '.':
                mat[x+1][y]='*'
                wq.append([x+1,y])
            if y + 1<c and mat[x][y+1] == '.':
                mat[x][y+1]='*'
                wq.append([x,y+1])

        for i in range(len(sq)):
            x,y=sq.popleft()

            if x-1>=0 and mat[x-1][y]=='.':
                mat[x-1][y]=mat[x][y]+1
                sq.append([x-1,y])
            if x - 1 >= 0 and mat[x-1][y] == 'D':
                print(mat[x][y]+1)
                return
            if y - 1 >= 0 and mat[x][y-1] == '.':
                mat[x][y-1]=mat[x][y]+1
                sq.append([x,y-1])
            if y - 1 >= 0 and mat[x][y-1] == 'D':
                print(mat[x][y]+1)
                return
            if x+1<r and mat[x+1][y] == '.':
                mat[x+1][y]=mat[x][y]+1
                sq.append([x+1,y])
            if x+1<r and mat[x+1][y] == 'D':
                print(mat[x][y]+1)
                return
            if y + 1<c and mat[x][y+1] == '.':
                mat[x][y+1]=mat[x][y]+1
                sq.append([x,y+1])
            if y + 1<c and mat[x][y+1] == 'D':
                print(mat[x][y]+1)
                return

    print("KAKTUS")

bfs()