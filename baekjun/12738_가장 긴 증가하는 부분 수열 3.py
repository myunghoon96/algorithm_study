# https://www.acmicpc.net/problem/12738
from bisect import bisect_left
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
ans = [nums[0]]
# dp = [1] * (N + 1)
# for i in range(N):
#     for j in range(0, i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

for i in range(N):
    if nums[i] > ans[-1]:
        ans.append(nums[i])
    else:
        idx = bisect_left(ans, nums[i])
        ans[idx] = nums[i]

print(len(ans))