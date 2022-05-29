# https://www.acmicpc.net/problem/2293

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for coin in coins:
    for money in range(K+1):
        if money-coin >=0:
            dp[money] += dp[money-coin] 

print(dp[K])