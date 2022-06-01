# https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left
#lis, binary search, 이분 탐색
#lis 수열 값은 안 맞을 수 있지만, lis 길이와 같음
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
lis = [nums[0]]

for i in range(1, N):
    if nums[i] > lis[-1]:
        lis.append(nums[i])
    else:
        num_idx = bisect_left(lis, nums[i])
        lis[num_idx] = nums[i]

# print(lis)
print(len(lis))