# https://www.acmicpc.net/problem/1309
import sys

N = int(sys.stdin.readline())

dp = [[0]*3 for _ in range(N)]

#left, right, all empty
dp[0] = [1,1,1]

for i in range(1, N):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901

print(sum(dp[-1])%9901)