#https://www.acmicpc.net/problem/11403

import sys
from collections import deque

vNum=int(sys.stdin.readline())
matrix=[]

graph=[[] for _ in range(vNum)]
for i in range(vNum):
    temp=list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)
    for j in range(vNum):
        if temp[j]==1:
            graph[i].append(j)


def bfs(start):
    visit=[0 for _ in range(vNum)]
    q=deque()
    q.append(start)
    # visit[start]=1
    h=[]
    while q:
        cur=q.popleft()
        h.append(cur)

        for node in graph[cur]:
            if visit[node]==0:
                q.append(node) 
                visit[node]=1

    return visit

for i in range(vNum):
    print(*bfs(i))