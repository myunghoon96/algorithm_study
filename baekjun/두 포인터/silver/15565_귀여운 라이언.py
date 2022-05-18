# https://www.acmicpc.net/problem/15565

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

l, r = 0, 0
ans = 10000000
lion = 0
if dolls[0] == 1:
    lion +=1

while l <= r and r < n:
    if lion < k:
        r += 1
        if r == n:
            break
        if dolls[r]== 1:
            lion += 1
    elif lion >= k:
        ans = min(ans, r-l+1)
        if dolls[l] == 1:
            lion -= 1
        l+=1
    # print(l,r, ans, lion)

if ans == 10000000:
    ans = -1
print(ans)