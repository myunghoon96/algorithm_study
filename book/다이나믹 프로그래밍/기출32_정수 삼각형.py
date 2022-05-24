# https://www.acmicpc.net/problem/1932

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(len(triangle[i])):
        dp[i][j] = triangle[i][j]

for i in range(1, n):
    for j in range(0, n):
        if j == 0 :
            dp[i][j] = dp[i][j] + dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j] + dp[i-1][j], dp[i][j] + dp[i-1][j-1])

print(max(dp[-1]))