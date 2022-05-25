N = 5
nums = [-15, -6, 1, 3, 7]

N = 7
nums = [-15, -4, 2, 8, 9, 13, 15]

N = 7
nums = [-15, -4, 3, 8, 9, 13, 15]

l, r = 0, N-1
ans = -1
while l <= r:
    mid_idx = (l+r)//2

    if nums[mid_idx] == mid_idx:
        ans = mid_idx
        break
    elif nums[mid_idx] < mid_idx:
        l = mid_idx + 1
    elif nums[mid_idx] > mid_idx:
        r = mid_idx - 1

print(ans)