#https://www.acmicpc.net/problem/1005

import sys
from collections import deque
input=sys.stdin.readline 
t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    times = [0]+list(map(int, input().split()))


    degree=[0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x].append(y)
        degree[y]+=1

    target = int(input())

    q=deque()
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)

    ans = [time for time in times]
    while q:
        cur = q.popleft()

        for next in graph[cur]:
            degree[next]-=1
            ans[next]=max(ans[next], ans[cur]+times[next])
            if degree[next]==0:
                q.append(next)

    print(ans[target])



