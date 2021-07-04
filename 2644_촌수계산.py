#https://www.acmicpc.net/problem/2644

import sys
from collections import deque

N = int(sys.stdin.readline())

start,end = map(int, (sys.stdin.readline().split()))

M = int(sys.stdin.readline())

graph=[[] for _ in range(N+1)]
visit=[0 for _ in range(N+1)]

def bfs():
    q=deque()
    q.append(start)
    visit[start]=1
    ans=0

    while q:
        cur=q.popleft()
        if cur==end:
            return visit[cur]-1
        
        for node in graph[cur]:
            if visit[node]==0:
                q.append(node)
                visit[node]=visit[cur]+1

    return -1



for _ in range(M):
    x,y = map(int, (sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

print(bfs())

