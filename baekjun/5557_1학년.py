# https://www.acmicpc.net/problem/5557

import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
target = nums[-1]

dp = [[0] * 21 for _ in range(N)]

dp[0][nums[0]] = 1

for i in range(1, N-1):
    num = nums[i]
    for j in range(0, 21):
        if dp[i-1][j] != 0 and j+num <= 20:
            dp[i][j+num] += dp[i-1][j]
        if dp[i-1][j] != 0 and j-num >= 0:
            dp[i][j-num] += dp[i-1][j]

# for e in dp:
#     print(e)

print(dp[-2][target])
