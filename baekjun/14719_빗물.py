# https://www.acmicpc.net/problem/14719
import sys
H, W = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
ans = 0

l, r = 0, W-1
max_l, max_r = heights[0], heights[-1]
while l < r:
    max_l = max(max_l, heights[l])
    max_r = max(max_r, heights[r])

    if max_l >= max_r:
        # print(l, r, max_l, max_r, max_r - heights[r])
        ans += (max_r - heights[r])
        r -= 1
        
    elif max_l < max_r:
        # print(l, r, max_l, max_r, max_l - heights[l])
        ans += (max_l - heights[l])
        l += 1

print(ans)

#ok
# ans = 0
# for i in range(1, W-1):
#     max_l = max(heights[:i])
#     max_r = max(heights[i+1:])

#     if heights[i] >= min(max_l, max_r):
#         continue
#     # print(i, (min(max_l, max_r) - heights[i]))
#     ans += (min(max_l, max_r) - heights[i])
# print(ans)