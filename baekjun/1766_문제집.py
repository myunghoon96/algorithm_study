#https://www.acmicpc.net/problem/2623

import sys
import heapq

n,m = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph=[[] for _ in range(n+1)]
degree=[0]*(n+1)

for i,info in enumerate(infos):
    pre, next = info
    graph[pre].append(next)
    degree[next]+=1

heap = []
for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(heap, i)
ans = []
while heap:
    cur = heapq.heappop(heap)
    ans.append(cur)
    for next_node in graph[cur]:
        degree[next_node]-=1
        if degree[next_node]==0:
            heapq.heappush(heap, next_node)


print(*ans)