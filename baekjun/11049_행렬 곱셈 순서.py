# https://www.acmicpc.net/problem/11049

import sys

N = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(N, nums)
dp = [[0]*N for _ in range(N)]

for d in range(1, N):
    for i in range(N-d):
        j = i + d
        if d == 1:
            dp[i][j] = nums[i][0] * nums[i][1] * nums[j][1]
            continue
        dp[i][j] = int(1e9)
        for k in range(i,j):
            # print((i,j,k), dp[i][j], dp[i][k], dp[k+1][j])
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i][0] * nums[k][1]* nums[j][1])

# for e in dp:
#     print(e)
print(dp[0][-1])