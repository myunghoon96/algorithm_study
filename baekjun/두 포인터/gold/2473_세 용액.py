# https://www.acmicpc.net/problem/2473
import sys
n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
# print(liquids)
ans_sum = sys.maxsize
ans_ele = []
# n - 2, because nums[i], l = nums[i+1]
for i in range(n-2):
    # tmp_list = liquids[:i] + liquids[i+1:]
    # l, r = 0, len(tmp_list)-1
    l, r = i+1, n-1
    while l < r:
        tmp_sum = liquids[l] + liquids[r] + liquids[i]
        if abs(ans_sum) > abs(tmp_sum):
            ans_sum = tmp_sum
            ans_ele = [liquids[i], liquids[l], liquids[r]]
            ans_ele.sort()

        if tmp_sum == 0: 
            break         
        elif tmp_sum > 0:
            r -= 1
        elif tmp_sum < 0:
            l += 1

# print(ans_sum)
print(*ans_ele)