#https://www.acmicpc.net/problem/11052
import copy 
N = int(input())
prices = [0] + list(map(int, input().split()))

dp = copy.deepcopy(prices)

for i in range(1, N+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[N])