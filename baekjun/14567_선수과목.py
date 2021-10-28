#https://www.acmicpc.net/problem/14567

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for info in infos:
    a,b =info
    graph[a].append(b)
    degree[b]+=1

q=deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

dp = [1]*(n+1)
while q:
    cur = q.popleft()
    for next in graph[cur]:
        degree[next]-=1
        dp[next]=max(dp[next], dp[cur]+1)
        if degree[next]==0:
            q.append(next)

print(*dp[1:])
