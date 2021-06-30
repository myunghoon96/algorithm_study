#https://www.acmicpc.net/problem/11724
from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())

node_graph=[[] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]

for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    node_graph[u].append(v)
    node_graph[v].append(u)


def bfs(node):
    q=deque()
    q.append(node)
    visit[node]=1
    while q:
        pop_node=q.popleft()
        for n in node_graph[pop_node]:
            if visit[n]==0:
                q.append(n)
                visit[n]=1
ans=0
for i in range(1, n+1):
    if visit[i]==0:
        bfs(i)
        ans+=1

print(ans)