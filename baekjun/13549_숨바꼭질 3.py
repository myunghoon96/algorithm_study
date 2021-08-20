#https://www.acmicpc.net/problem/13549

from collections import deque

def bfs(a,b):
    q = deque()
    v = [0 for _ in range(100001)]
    q.append((a,0))
    v[a]=1

    while q:
        cur, cnt= q.popleft()

        if cur==b:
            print(cnt)
            return

        if 0<=cur*2<=100000 and v[cur*2]==0 and cur!=0:
            v[cur*2]=1
            q.appendleft((cur*2,cnt))

        if cur+1<=100000 and v[cur+1]==0:
            v[cur+1]=1
            q.append((cur+1,cnt+1))

        if cur-1>=0 and v[cur-1]==0:
            v[cur-1]=1
            q.append((cur-1,cnt+1))



    return

a, b = map(int,input().split())
bfs(a,b)
