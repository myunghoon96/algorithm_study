# https://www.acmicpc.net/problem/10775

import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

airs = [int(sys.stdin.readline()) for _ in range(P)]
parents = [i for i in range(G+1)]

def find_parents(a):
    if a != parents[a]:
        parents[a] = find_parents(parents[a])
    return parents[a]

def union(a, b):
    a, b = find_parents(a), find_parents(b)
    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b

ans = 0
for air in airs:
    parent = find_parents(air)

    if parent == 0:
        break

    union(parent, parent-1)
    ans += 1

print(ans)