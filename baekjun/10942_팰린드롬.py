#https://www.acmicpc.net/problem/10942

import sys
input=sys.stdin.readline

n=int(input())
s=list(map(int,input().split()))
m=int(input())

dp=[[0 for j in range(n)] for i in range(n)]

for i in range(n):
    dp[i][i]=1

for i in range(n-1):
    if s[i]==s[i+1]:
        dp[i][i+1]=1


for i in range(2,n):
    for j in range(n-i):
        start=j
        end=j+i
        if s[start]==s[end] and dp[start+1][end -1]==1:
            dp[start][end]=1

for i in range(m):
    start, end= map(int,input().split())
    print(dp[start-1][end-1])
