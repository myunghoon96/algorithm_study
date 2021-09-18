input = '02984'

ans = 0
for num in input:
    if int(num) > 1 and ans > 1:
        ans*=int(num)
    else:
        ans+=int(num)

print(ans)