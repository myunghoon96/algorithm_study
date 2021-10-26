#https://www.acmicpc.net/problem/2252

import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

compare = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for c in compare:
    a,b= c
    graph[a].append(b)
    degree[b]+=1

q=deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)
ans = []
while q:
    node = q.popleft()
    ans.append(node)
    for connect_node in graph[node]:
        degree[connect_node]-=1
        if degree[connect_node]==0:
            q.append(connect_node)   

print(*ans)

