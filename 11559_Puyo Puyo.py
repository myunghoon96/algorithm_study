#https://www.acmicpc.net/problem/11559

import sys
from collections import deque
r=12
c=6
mat=[[0]*c for _ in range(r)]

for i in range(r):
    temp=sys.stdin.readline().strip()
    for j in range(c):
        if temp[j]=='R':
            mat[i][j]=1

        elif temp[j]=='G':
            mat[i][j]=2

        elif temp[j]=='B':
            mat[i][j]=3

        elif temp[j]=='P':
            mat[i][j]=4

        elif temp[j]=='Y':
            mat[i][j]=5



def bfs(x,y):
    global flag
    v=[[0]*c for _ in range(r)]

    q=deque()
    q.append((x,y))
    d=[]
    color=mat[x][y]
    v[x][y]=1

    while q:
        x,y=q.popleft()
        d.append((x,y))

        if x-1>=0 and mat[x-1][y]==color and v[x-1][y]==0:
            q.append((x-1,y))
            v[x-1][y]=1
        if y - 1 >= 0 and mat[x][y-1]==color and v[x][y-1]==0:
            q.append((x,y-1))
            v[x][y - 1]= 1
        if x+1<r and mat[x+1][y]==color and v[x+1][y]==0:
            q.append((x+1,y))
            v[x + 1][y]=1
        if y + 1<c and mat[x][y+1]==color and v[x][y+1]==0:
            q.append((x,y+1))
            v[x][y + 1]=1

    if len(d)>=4:
        # print("delete", d)
        flag=1
        for e in d:
            x=e[0]
            y=e[1]
            mat[x][y]=0


ans=0
flag=1
while flag:

    cl=[]
    ans+=1
    flag=0
    for i in range(r):
        for j in range(c):
            if mat[i][j]!=0:
                bfs(i,j)
                cl.append((i,j))
    # print("cl is ", cl[::-1])
    for e in cl[::-1]:
        x=e[0]
        y=e[1]
        if mat[x][y]!=0:
            color=mat[x][y]
            status=0
            if x+1<r:
                index = 1
                while x+index<r and mat[x+index][y]==0:
                    status=1
                    index+=1
            if status:
                mat[x][y] = 0
                mat[x+index-1][y]=color

print(ans-1)
    # for a in mat:
    #     print(a)
    # print()