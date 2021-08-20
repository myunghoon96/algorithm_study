#https://www.acmicpc.net/problem/11725

import sys
from collections import deque 

N = int(sys.stdin.readline())

graph=[[] for _ in range(N+1)]
visit=[0 for _ in range(N+1)]

def bfs():
    q=deque()
    q.append(1)
    visit[1]=1

    while q:
        cur=q.popleft()

        for node in graph[cur]:
            if visit[node]==0:
                q.append(node)
                visit[node]=cur

    return -1




for _ in range(N-1):
    x,y = map(int, (sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

bfs()

for e in visit[2:]:
    print(e)
