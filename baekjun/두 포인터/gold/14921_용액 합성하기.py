# https://www.acmicpc.net/problem/14921

n = int(input())
a = list(map(int, input().split()))
ans = 1e9

l, r = 0, n-1
while l < r:
    tmp_sum = a[l]+a[r]
    if abs(ans) > abs(tmp_sum):
        ans = tmp_sum

    if tmp_sum > 0 :
        r -= 1
    elif tmp_sum == 0:
        break
    elif tmp_sum < 0:
        l += 1

print(ans)
    
