# https://www.acmicpc.net/problem/2631
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

#lis
dp = [1] * N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(N - max(dp))
