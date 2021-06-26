#https://www.acmicpc.net/problem/10026

n=int(input())
l=[]
l2=[]
v=[[0]*n for _ in range(n)]
for i in range(n):
    temp=input()
    l.append(temp)
    l2.append(temp.replace("G","R"))


def dfs(x,y,l):

    q=[]
    q.append((x,y))
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]

    while q:
        x,y=q.pop()

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<=xx<n and 0<=yy<n and l[xx][yy]==l[x][y] and v[xx][yy]==0:
                v[xx][yy]=1
                q.append((xx,yy))


ans=0
for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            dfs(i,j,l)
            ans+=1

ans2=0
v=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            dfs(i,j,l2)
            ans2+=1

print(ans, ans2)
