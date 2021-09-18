# N-1 or N/k to make N = 1
n = 25
k = 3
ans = 0

while True:
    
    minus = n - (n//k)*k
    ans+=minus
    n = n-minus

    if n<k:
        break

    n = n//k 
    ans+=1

    if n<k:
        break

minus = n-1
n-=minus
ans+=minus
print(n)
print(ans)