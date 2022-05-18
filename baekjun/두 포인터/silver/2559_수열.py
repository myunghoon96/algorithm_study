# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))

tmp_sum = 0
l, r = 0, k-1
for i in range(k):
    tmp_sum += temperatures[i]
ans = tmp_sum

while r < n-1:
    tmp_sum -= temperatures[l]
    l += 1
    r += 1
    tmp_sum += temperatures[r]
    ans = max(ans, tmp_sum)

print(ans)