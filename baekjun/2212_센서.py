#https://www.acmicpc.net/problem/2212

import sys

n=int(sys.stdin.readline().strip())
k=int(sys.stdin.readline().strip())
l=list(map(int, sys.stdin.readline().split()))

l.sort()
g=[]

if k>=n:
    print(0)

else: 
    for i in range(1,n):
        g.append(l[i]-l[i-1])
    
    g.sort()
    for i in range(k-1):
        g.pop()
    
    print(sum(g))