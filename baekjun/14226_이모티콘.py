#https://www.acmicpc.net/problem/14226

import sys
from collections import deque

v = [[-1] * 1001 for _ in range(1001)]
def bfs(a):
    global v
    q = deque()
    q.append((1,0))
    v[1][0]=0

    while q:
        cur, cb= q.popleft()

        if 0<cur<=1000 and v[cur][cur]==-1:
            q.append((cur,cur))
            v[cur][cur]=v[cur][cb]+1

        if 0<cur+cb<=a and v[cur+cb][cb]==-1:
            q.append((cur+cb,cb))
            v[cur+cb][cb]=v[cur][cb]+1


        if cur-1>=0 and v[cur-1][cb]==-1:
            q.append((cur-1,cb))
            v[cur-1][cb]=v[cur][cb]+1

    return

a=int(input())
bfs(a)
ans=sys.maxsize
for e in v[a]:
    if e!=-1:
        ans=min(ans,e)
print(ans)