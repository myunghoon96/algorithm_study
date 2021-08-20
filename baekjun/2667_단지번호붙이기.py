#https://www.acmicpc.net/problem/2667
n=int(input())
matrix=[[0]*(n) for i in range(n)]
visit=[[0]*(n) for i in range(n)]
num=0
for i in range(n):
    temp=input()
    for k in range(n):
        matrix[i][k]=int(temp[k])

def dfs(x,y):
    visit[x][y]=1
    matrix[x][y] = 5
    global num
    num+=1
    if x+1<n and visit[x+1][y]==0 and matrix[x+1][y]==1:
        dfs(x+1,y)
    if x-1>=0 and visit[x-1][y]==0 and matrix[x-1][y]==1:
        dfs(x-1,y)
    if y+1<n and visit[x][y+1]==0 and matrix[x][y+1]==1:
        dfs(x,y+1)
    if y-1>=0 and visit[x][y-1]==0 and matrix[x][y-1]==1:
        dfs(x,y-1)
l=[]
ans=0
for i in range(n):
    for k in range(n):
        if visit[i][k]==0 and matrix[i][k]==1:
            dfs(i,k)
            l.append(num)
            num=0
            ans+=1

print(ans)
l.sort()
for e in l:
    print(e)