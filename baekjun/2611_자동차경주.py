#https://www.acmicpc.net/problem/2611

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
infos = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for info in infos:
    p,q,r = info
    graph[p].append((q,r))
    degree[q]+=1

q=deque()
q.append(1)
ans = [0]*(n+1)
visit = [[] for _ in range(n+1)]
visit[1]=[1]
pre_list = [0]*(n+1)
while q:
    cur = q.popleft()
    ans.append(cur)
    for next, score in graph[cur]:
        degree[next]-=1
        if ans[cur]+score > ans[next]:
            ans[next]=ans[cur]+score
            visit[next]=visit[cur]+[next]
            # pre_list[next]=cur
        if degree[next]==0:
            q.append(next)

print(ans[1])
print(*visit[1])
# pre_node=1
# pre_visit = [pre_node]
# while True:
#     pre_node = pre_list[pre_node]
#     pre_visit.append(pre_node)
#     if pre_node==1:
#         break
# print(*pre_visit[::-1])