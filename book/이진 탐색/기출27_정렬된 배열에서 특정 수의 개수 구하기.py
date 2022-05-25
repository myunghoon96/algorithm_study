from bisect import bisect_left, bisect_right

N, x = 7, 2
nums = [1, 1, 2, 2, 2, 2, 3]

ans = bisect_right(nums, x) - bisect_left(nums, x)

print(ans) if ans != 0 else print(-1)