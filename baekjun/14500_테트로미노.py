#https://www.acmicpc.net/problem/14500
import sys

n, m = map(int, sys.stdin.readline().split())
# print(n,m)

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(matrix)
visit = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = 0
def find(x, y): #ㅏ,ㅓ,ㅗ,ㅜ
    global ans
    l = [[(0,-1), (1,0), (-1,0)],[(0,1),(1,0), (-1,0)],[(0,1), (0,-1), (-1,0)],[(0,1), (0,-1), (1,0)]]
    for combi in l:
        score=matrix[x][y]
        for i in range(3):
            xx, yy= x+combi[i][0], y+combi[i][1]
            if 0<=xx<n and 0<=yy<m:
               score+=matrix[xx][yy]
               if i==2:
                   if score > ans:
                       ans = score
                    
    return

def dfs(x, y, cnt, score):
    global ans
    if cnt ==3:
        if score > ans:
            ans = score
        return

    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and visit[xx][yy]==0:
            visit[xx][yy]=1
            dfs(xx,yy,cnt+1,score+matrix[xx][yy])
            visit[xx][yy]=0

for i in range(n):
    for j in range(m):
        visit[i][j]=1
        dfs(i,j,0,matrix[i][j])
        visit[i][j]=0
        find(i,j)

# print(ans_list)
print(ans)