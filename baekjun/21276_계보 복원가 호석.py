#https://www.acmicpc.net/problem/21276

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
members = list(input().split())
m = int(input())
infos = [list(input().split()) for _ in range(m)]

graph=dict()
degree=dict()
child=dict()
for i in range(n):
    graph[members[i]]=[]
    degree[members[i]]=0
    child[members[i]]=[]
    
for info in infos:
    x,y = info
    graph[y].append(x)
    degree[x]+=1

q=deque()
roots=[]
for member in members:
    if degree[member]==0:
        q.append(member)
        roots.append(member)

while q:
    cur = q.popleft()
    for next in graph[cur]:
        degree[next]-=1
        if degree[next]==0:
            q.append(next)
            child[cur].append(next)
# print("roots ", sorted(roots))
child_order=sorted(list(child))
# print("child ", sorted(child_order))
print(len(roots))
print(*sorted(roots))
for c in child_order:
    print(c, len(child[c]), *sorted(child[c]))