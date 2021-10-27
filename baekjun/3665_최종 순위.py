#https://www.acmicpc.net/problem/3665

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    status_imp = False
    status_not_find = False
    n = int(input())
    last = list(map(int, input().split()))
    m = int(input())
    infos = [list(map(int, input().split())) for _ in range(m)]

    graph = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[last[i]].append(last[j])
            degree[last[j]]+=1

    for info in infos:
        a,b = info
        if a in graph[b]:
            graph[b].remove(a)
            degree[a]-=1
            graph[a].append(b)
            degree[b]+=1
        else:
            graph[a].remove(b)
            degree[b]-=1
            graph[b].append(a)
            degree[a]+=1

    q=deque()
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)

    ans = []
    if len(q)==0:
        status_imp=True
    while q:
        cur = q.popleft()
        ans.append(cur)
        if len(q)>1:
            status_not_find=True
        for next in graph[cur]:
            degree[next]-=1
            if degree[next]==0:
                q.append(next)

    if status_imp or len(ans)<n: 
        print("IMPOSSIBLE")
    elif status_not_find:
        print("?")
    else:
        print(*ans)