#https://www.acmicpc.net/problem/4358

import sys

d=dict()
total=0

while 1:
    temp=sys.stdin.readline().strip()

    if temp=='':
        break

    total+=1
    if d.get(temp)==None:
        d[temp]=1
    else:
        d[temp]+=1

l=sorted(d)

for e in l:
    print('%s %.4f' %(e, d[e]/total*100))