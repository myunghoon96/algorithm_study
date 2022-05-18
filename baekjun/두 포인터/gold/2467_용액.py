# https://www.acmicpc.net/problem/2467
# https://www.acmicpc.net/problem/2470
# https://www.acmicpc.net/problem/14921

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans_sum = a[0] + a[n-1]
ans = [a[0], a[n-1]]
l, r = 0, n-1
while l < r:
    tmp_sum = a[l]+a[r]
    if abs(ans_sum) > abs(tmp_sum):
        ans_sum = tmp_sum
        ans = [a[l], a[r]]
    if tmp_sum > 0 :
        r -= 1
    elif tmp_sum == 0:
        break
    elif tmp_sum < 0:
        l += 1

# print(ans_sum)
print(*ans)
