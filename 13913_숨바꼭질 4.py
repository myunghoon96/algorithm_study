#https://www.acmicpc.net/problem/13913

from collections import deque
n,k=map(int,input().split())

v=[-1 for _ in range(100001)]


def bfs(x):
    q=deque()
    q.append((x,0))
    v[x]=x
    while q:
        x,cnt=q.popleft()

        if x==k:
            print(cnt)

            a=k
            ans=[]
            ans.append(k)
            while a!=n:
                ans.append(v[a])
                a=v[a]

            print(*ans[::-1])

            return

        if 0<=x+1<=100000 and v[x+1]==-1:
            v[x+1]=x
            q.append((x+1,cnt+1))

        if 0<=x-1<=100000 and v[x-1]==-1:
            v[x-1]=x
            q.append((x-1,cnt+1))

        if 0<=x*2<=100000 and v[x*2]==-1:
            v[x*2]=x
            q.append((x*2,cnt+1))

bfs(n)