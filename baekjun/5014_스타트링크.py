#https://www.acmicpc.net/problem/5014

from collections import deque
f,s,g,u,d=map(int,input().split())
q=deque()
v=[0 for _ in range(f+1)]
def bfs():

    q.append((s,0))

    while q:
        cur, cnt= q.popleft()

        if cur==g:
            print(cnt)
            return

        if cur+u<=f and v[cur+u]==0:
            v[cur+u]=1
            q.append((cur+u,cnt+1))

        if cur-d>=1 and v[cur-d]==0:
            v[cur-d]=1
            q.append((cur-d,cnt+1))


    print("use the stairs")

bfs()
