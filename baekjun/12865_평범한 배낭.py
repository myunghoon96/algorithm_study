#https://www.acmicpc.net/problem/12865

import sys
input=sys.stdin.readline
n,k = map(int, input().split())
dp =[[0]*(k+1) for _ in range(n+1)]
info=[[0,0]]

for i in range(n+1):
    pair=list(map(int,(input().split())))
    info.append(pair)

for i in range(1,n+1):
    for j in range(1,k+1):
        w=info[i][0]
        v=info[i][1]
        if j>=w:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][k])