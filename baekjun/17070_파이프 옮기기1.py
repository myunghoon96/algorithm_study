#https://www.acmicpc.net/problem/17070


import sys

n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans=0
def dfs(x,y,t):
#t:0 hori, t:1 verti, t:2 daegak

    global ans
    if x==n-1 and y==n-1:
        ans+=1
        return

#hori, daegak   move right
    if t==0 or t==2:
        if 0<=y+1<n and mat[x][y+1]==0:
            dfs(x,y+1,0)    


#verti, daegak  move down
    if t==1 or t==2:
        if 0<=x+1<n and mat[x+1][y]==0:
            dfs(x+1,y,1)   


#hori,verti,daegak   move right under
    if t==0 or t==1 or t==2:
        if 0<=x+1<n and 0<=y+1<n and mat[x][y+1]==0 and mat[x+1][y]==0 and mat[x+1][y+1]==0:
            dfs(x+1,y+1,2)   

    return

dfs(0,1,0)
print(ans)