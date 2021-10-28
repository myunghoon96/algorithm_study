#https://www.acmicpc.net/problem/2637

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
infos = [list(map(int,input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
matrix = [[0]*(n+1) for _ in range(n+1)]
for info in infos:
    x,y,k = info
    graph[y].append((x,k))
    degree[x]+=1

q=deque()
basics = []
for i in range(1,n+1):
    if degree[i]==0: #기본 부품
        q.append(i)
        #matrix[i]=0
        basics.append(i)

while q:
    cur = q.popleft()
    for next,need in graph[cur]:
        if cur in basics: #cur 기본 부품
            matrix[next][cur]+=need
        else: #cur 중간 부품
            for i in range(1,n+1):
                matrix[next][i]+=matrix[cur][i]*need
        degree[next]-=1
        if degree[next]==0:
            q.append(next)

for b in basics:
    print(b, matrix[-1][b])