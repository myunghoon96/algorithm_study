# https://www.acmicpc.net/problem/14002

import sys

input = sys.stdin.readline

A = int(input().rstrip())
nums = list(map(int, input().split()))
dp = [1] * (A)

max_len = -1
max_str = []
for i in range(A):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            # max_len = max(max_len, dp[i])

# print(dp)
max_len = max(dp)
print(max_len)

target = max_len
for i in range(A-1, -1, -1):
    if dp[i] == target:
        max_str.append(nums[i])
        target -=1

print(*max_str[::-1])