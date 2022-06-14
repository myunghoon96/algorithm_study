# https://www.acmicpc.net/problem/1890

import sys
sys.setrecursionlimit(int(10e6))
N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0
dp = [[0] *N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        val = matrix[i][j]
   
        if i + val < N:
            dp[i+val][j] += dp[i][j]
        if j + val < N:
            dp[i][j+val] += dp[i][j] 

    # print()
    # for e in dp:
    #     print(e)

print(dp[-1][-1])

# def dfs(x, y):
#     global ans
#     if x == N-1 and y == N-1:
#         ans += 1
#         return

#     val = matrix[x][y]
#     if x + val < N:
#         dfs(x + val, y)
#     if y + val < N:
#         dfs(x, y + val)

# dfs(0, 0)
# print(ans)