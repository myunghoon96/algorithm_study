#https://www.acmicpc.net/problem/9663

import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

row=[0 for _ in range(n)]
sl=[0 for _ in range((2*n-1))]
bsl=[0 for _ in range((2*n-1))]

idx=0
ans=0
def f(idx):
    global ans

    if idx==n:
        ans+=1
        return

    for col in range(n):
        if row[col]==0 and sl[idx+col]==0 and bsl[idx-col+n-1]==0:
            row[col] = 1
            sl[idx+col] = 1
            bsl[idx-col+n-1] = 1
            f(idx+1)
            row[col] = 0
            sl[idx+col] = 0
            bsl[idx-col+n-1] = 0


f(0)
print(ans)





