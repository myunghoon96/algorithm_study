# https://www.acmicpc.net/problem/2018

n = int(input())
ans = 1
l,r = 1,1
tmp_sum = 1
# while l < n and r < n:
while l <= n//2:
    if tmp_sum == n:
        ans += 1
        tmp_sum -= l
        l += 1
        r += 1
        tmp_sum += r
        
    elif tmp_sum < n:
        r += 1
        tmp_sum += r
        
    elif tmp_sum > n:
        tmp_sum -= l
        l += 1

print(ans)