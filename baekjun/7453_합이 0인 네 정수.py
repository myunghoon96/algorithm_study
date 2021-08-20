#https://www.acmicpc.net/problem/7453

import sys
ab=dict()
cd=dict()
a,b,c,d=[],[],[],[]

n=int(input())
for i in range(n):
    t1,t2,t3,t4=map(int,sys.stdin.readline().split())
    a.append(t1)
    b.append(t2)
    c.append(t3)
    d.append(t4)

for e1 in a:
    for e2 in b:
        temp=e1+e2
        if temp in ab:
            ab[temp]+=1
        else:
            ab[temp]=1

ans=0
for e1 in c:
    for e2 in d:
        temp=-1*(e1+e2)
        if temp in ab:
            ans+=ab[temp]

print(ans)