# https://www.acmicpc.net/problem/1976

import sys

def find_parent(parents, a):
    if a != parents[a]:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
parents = [i for i in range(N)]
for i in range(N):
    infos = list(map(int, (sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if infos[j] == 1:
            if find_parent(parents, i) != find_parent(parents, j):
                union(parents, i, j)

plan = list(map(int, (sys.stdin.readline().rstrip().split())))

# print(parents)

parent_set = set()
for p in plan:
    parent_set.add(find_parent(parents, p-1))

if len(parent_set) == 1:
    print("YES")
else:
    print("NO")