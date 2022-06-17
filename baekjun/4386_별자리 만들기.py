# https://www.acmicpc.net/problem/4386

import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
stars = []
for i in range(N):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((i, x, y))

stars.sort(key = lambda x:(x[1],x[2],x[0]))

def calculate_distance(x1, y1, x2, y2):
    return (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5

edges = []
for i in range(N):
    for j in range(i+1, N):
        a, x1, y1 = stars[i]
        b, x2, y2 = stars[j]
        dist = calculate_distance(x1,y1,x2,y2)
        edges.append((dist, a, b))

edges.sort()

parents = [i for i in range(N)]
def find_parent(a):
    if a != parents[a]:
        parents[a] = find_parent(parents[a])
    return parents[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b :
        parents[b] = a
    elif a > b:
        parents[a] = b

ttl_cost = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union(a, b)
        ttl_cost += cost

print(round(ttl_cost, 2))