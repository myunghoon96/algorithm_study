# https://www.acmicpc.net/problem/2294

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [int(1e9)]*(K+1)
for coin in coins:
    if coin >= K:
        continue
    dp[coin] = 1

for coin in coins:
    if coin >= K:
        continue
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[K] == int(1e9):
    dp[K] = -1
print(dp[K])
