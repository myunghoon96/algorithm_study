# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
nums = list(map(int, input().split()))
l, r = 0, 0
tmp_sum = nums[0]
ans = 0

while l < n and r < n:
    if tmp_sum == m:
        tmp_sum -= nums[l]
        l += 1
        ans += 1

    else:
        if tmp_sum > m:
            tmp_sum -= nums[l]
            l += 1
            
        elif tmp_sum < m:
            r += 1
            if r >= n:
                break
            tmp_sum += nums[r]


print(ans)