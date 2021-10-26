#https://www.acmicpc.net/problem/2056

import sys
from collections import deque

n = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
times=[0]*(n+1)
degree=[0]*(n+1)
dp=[0]*(n+1)

graph = [[] for _ in range(n+1)]

for i,info in enumerate(infos):
    i+=1
    times[i]=info[0]
    dp[i]=info[0]
    num = info[1]
    pre_works = info[2:]
    for pre in pre_works:
        graph[pre].append(i)
        degree[i]+=1

q=deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

orders=[]
while q:
    cur = q.popleft()
    orders.append(cur)
    for next_node in graph[cur]:
        degree[next_node]-=1
        dp[next_node]=(max(dp[next_node], times[next_node]+dp[cur]))
        if degree[next_node]==0:
            q.append(next_node)

print(max(dp))