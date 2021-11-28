#https://www.acmicpc.net/problem/14501

import sys

n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i+l[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], dp[i+l[i][0]]+l[i][1])

print(dp[0])
