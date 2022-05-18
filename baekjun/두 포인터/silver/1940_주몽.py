# https://www.acmicpc.net/problem/1940

n = int(input())
m = int(input())
materials = list(map(int, input().split()))

materials.sort()
l, r = 0, n-1
ans = 0
while l < r:
    if materials[l] + materials[r] == m :
        r -= 1
        ans += 1
    elif materials[l] + materials[r] < m:
        l += 1
    elif materials[l] + materials[r] > m:
        r -= 1
print(ans)