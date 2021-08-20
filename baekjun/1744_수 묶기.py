#https://www.acmicpc.net/problem/1744

import sys

n=int(sys.stdin.readline().strip())

neg=[]
pos=[]
one=[]
zer=[]
for i in range(n):
    temp=int(sys.stdin.readline().strip())
    if temp<0:
        neg.append(temp)
    elif temp==0:
        zer.append(temp)
    elif  temp==1:
        one.append(temp)
    else:
        pos.append(temp)

neg.sort()
pos.sort(reverse=True)
ans=0

ans+=len(one)

if len(pos)%2==0:
    index=0
    while index<len(pos):
        ans+=pos[index]*pos[index+1]
        index+=2
else:
    index=0
    while index<len(pos)-1:
        ans+=pos[index]*pos[index+1]
        index+=2
    ans+=pos[-1]

if len(neg)%2==0:
    index=0
    while index<len(neg):
        ans+=neg[index]*neg[index+1]
        index+=2
else:
    index=0
    while index<len(neg)-1:
        ans+=neg[index]*neg[index+1]
        index+=2
    if len(zer)==0:
        ans+=neg[-1]

print(ans)