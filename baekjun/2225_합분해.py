# https://www.acmicpc.net/problem/2225

N, K = map(int,(input().split()))
dp = [[0] * (K+1) for _ in range(N+1)]

for j in range(1, K+1):
    dp[1][j] = j

for i in range(1, N+1):
    dp[i][1] = 1

for i in range(2, N+1):
    for j in range(2, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# for e in dp:
#     print(e)

print(dp[-1][-1] % 1000000000)