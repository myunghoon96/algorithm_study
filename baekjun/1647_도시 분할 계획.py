# https://www.acmicpc.net/problem/1647
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
parents = [i for i in range(N+1)]

def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(x,y):
    x, y = find_parent(x), find_parent(y)

    if x < y:
        parents[y] = parents[x]
    elif x > y:
        parents[x] = parents[y] 

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

max_cost = -1
ttl_cost = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        max_cost = max(max_cost, c)
        ttl_cost += c
print(ttl_cost - max_cost)