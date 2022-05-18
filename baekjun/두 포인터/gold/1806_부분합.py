# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 0
ans_sum = nums[0]
ans_cnt = 100001

while True:
    if l == n:
        break
    # print(l,r, ans_cnt, ans_sum)
    if ans_sum >= s:
        ans_cnt = min(ans_cnt, r -l + 1)
        ans_sum -= nums[l]
        l += 1
    else:
        if r + 1 == n:
            break
        r += 1
        ans_sum += nums[r]
    # print(l,r,ans_cnt,ans_sum)

if ans_cnt == 100001:
    print(0)
else:
    print(ans_cnt)