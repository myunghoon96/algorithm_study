
n, m = 4, 6
cakes = [19, 15, 10, 17]

ans = -1
cakes.sort()

l, r = 0, cakes[-1]
while l <= r:
    mid = l + (r - l)//2
    height = mid
    give = 0

    for cake in cakes:
        if cake > height:
            give += (cake-height)
    # print(l, r, height, give)

    if give >= m:
        ans = max(ans, height)
        l = mid + 1

    elif give < m:
        r = mid - 1 

print(ans)
