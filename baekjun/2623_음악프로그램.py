#https://www.acmicpc.net/problem/2623

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph=[[] for _ in range(n+1)]
degree=[0]*(n+1)

for i,info in enumerate(infos):
    num=info[0]
    singers=info[1:]
    for j in range(len(singers)):
        for k in range(j+1,len(singers)):
            graph[singers[j]].append(singers[k])
            degree[singers[k]]+=1

q=deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)
ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for next_node in graph[cur]:
        degree[next_node]-=1
        if degree[next_node]==0:
            q.append(next_node)

if len(ans)<n:
    print(0)
else:
    for e in ans:
        print(e)