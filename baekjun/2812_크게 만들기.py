#https://www.acmicpc.net/problem/2812

import sys
input=sys.stdin.readline

n, k=map(int,input().split())
s=input()
l=[]
tk=k

for i in range(n):
    while tk>0 and l and l[-1]<s[i]:
        l.pop()
        tk-=1
    l.append(s[i])

for i in range(n-k):
    print(l[i], end="")