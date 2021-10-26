#https://www.acmicpc.net/problem/1516

import sys
from collections import deque

n = int(sys.stdin.readline())
instructions = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
times = [0]*(n+1)
ans = [0]*(n+1)
for building,ins in enumerate(instructions):
    building+=1
    times[building] = ins[0]
    pre = ins[1:-1]
    ans[building] = ins[0]
    
    for p in pre:
        graph[p].append(building)
        degree[building]+=1

q=deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

while q:
    cur = q.popleft()
    for connect_node in graph[cur]:
        degree[connect_node]-=1
        ans[connect_node]= max(ans[connect_node], times[connect_node]+ans[cur])
        if degree[connect_node]==0:
            q.append(connect_node)

for i in range(1,n+1):
    print(ans[i])