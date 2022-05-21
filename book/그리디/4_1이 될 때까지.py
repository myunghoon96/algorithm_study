n, k = 25, 5
ans = 0

while n != 1:

    if n%k == 0:
        n = n // k
        ans += 1

    else:
        # n -= 1
        # ans += 1
        ans += n%k
        n -= (n%k)
        

print(ans)