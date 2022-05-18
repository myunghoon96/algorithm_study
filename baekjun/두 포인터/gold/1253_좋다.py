# https://www.acmicpc.net/problem/1253

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0

for i in range(n):
    tmp_list = nums[:i] + nums[i+1:]
    target = nums[i]
    l, r = 0, len(tmp_list)-1

    while l < r:
        tmp_sum = tmp_list[l] + tmp_list[r]
        if  tmp_sum == target:
            ans += 1
            break
        elif tmp_sum > target:
            r -= 1
        elif tmp_sum < target:
            l += 1
print(ans)   
