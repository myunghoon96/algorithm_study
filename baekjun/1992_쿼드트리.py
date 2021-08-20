#https://www.acmicpc.net/problem/1992

import sys
input=sys.stdin.readline

n=int(input())
l=[]

for i in range(n):
    temp=input().strip()
    l.append(temp)

ans=""
def f(n, x, y):
    global ans

    zeroOne=int(l[x][y])

    for i in range(x,x+n):
        for k in range(y,y+n):
            if int(l[i][k]) != zeroOne:
                n=n//2
                ans+='('
                f(n, x,y)
                f(n, x, y+n)
                f(n, x+n, y)
                f(n, x+n, y+n)
                ans+=')'
                return

    ans+=str(zeroOne)
    return
f(n,0,0)
print(ans)
