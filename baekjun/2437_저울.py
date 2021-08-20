#https://www.acmicpc.net/problem/2437

n=int(input())

l=list(map(int,input().split()))

l.sort()

t=0
temp=0
for i in range(n):
    if t+1 >= l[i]:
        t+=l[i]

    else:
        break

print(t+1)