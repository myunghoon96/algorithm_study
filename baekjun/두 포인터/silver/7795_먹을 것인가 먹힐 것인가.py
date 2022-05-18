t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    l, r = 0, 0
    ans = 0
    while l < n and r < m:
        if a[l] > b[r]:
            ans += (n-l)
            r += 1
        else:
            l += 1
    print(ans)