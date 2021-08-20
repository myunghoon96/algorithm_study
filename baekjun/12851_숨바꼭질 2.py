#https://www.acmicpc.net/problem/12851

from collections import deque
ans1, ans2=0,0
def bfs(a,b):
    global ans1,ans2
    q = deque()
    v = [0 for _ in range(100001)]
    q.append((a,0))
    v[a]=1
    status=0

    while q:
        cur, cnt= q.popleft()

        v[cur]=1

        if cur==b and status==0:
            ans1=cnt
            ans2+=1
            status=1
            continue

        if cur==b and status!=0 and cnt==ans1:
            ans2+=1
            continue

        if cur*2<=100000 and v[cur*2]==0:
            # v[cur*2]=1
            q.append((cur*2,cnt+1))

        if cur+1<=100000 and v[cur+1]==0:
            # v[cur+1]=1
            q.append((cur+1,cnt+1))

        if 0<=cur-1 and v[cur-1]==0:
            # v[cur-1]=1
            q.append((cur-1,cnt+1))

    return

a, b = map(int,input().split())
bfs(a,b)
print(ans1)
print(ans2)