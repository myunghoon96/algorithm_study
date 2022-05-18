# https://www.acmicpc.net/problem/2230

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

ans = 2e9
l, r = 0, 1
while l < n and r < n:
    tmp_diff = nums[r] - nums[l]
    if tmp_diff == m:
        ans = min(ans, tmp_diff)
        break
    elif tmp_diff > m :
        ans = min(ans, tmp_diff)
        l += 1
    else:
        #tmp_diff < m
        r += 1

print(ans)