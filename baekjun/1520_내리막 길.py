# https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
dp = [[-1] * N for _ in range(M)]
ans = 0

def dfs(x,y):
    # print(x,y)
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < M and 0 <= yy < N and matrix[xx][yy] < matrix[x][y]:
            dp[x][y] += dfs(xx,yy)
    
    return dp[x][y]

dfs(0,0)
# for e in dp:
#     print(e)
print(dp[0][0])