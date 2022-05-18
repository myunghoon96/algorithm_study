#https://www.acmicpc.net/problem/3273

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
x = int(input())

l, r = 0, n-1
ans = 0
a.sort()

while l < r:
    if a[l] + a[r] == x:
        ans+= 1
        r -= 1
    else:
        if a[l] + a[r] < x:
            l += 1
        elif a[l] + a[r] > x:
            r -= 1
print(ans)

# 시간 초과
# ans = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if a[i] + a[j] == x:
#             ans += 1
# print(ans)