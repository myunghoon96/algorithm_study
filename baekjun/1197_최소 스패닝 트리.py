# https://www.acmicpc.net/problem/1197

def find_parent(parents, x):
    
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])

    return parents[x]

def union(parents, a, b):

    parent_a, parent_b = find_parent(parents, a), find_parent(parents, b)

    if parent_a < parent_b:
        parents[parent_b] = parent_a
    elif parent_a > parent_b:
        parents[parent_a] = parent_b

V, E = map(int, input().split())
parents = [i for i in range(V+1)]

infos = []
for _ in range(E):
    a, b, c = map(int, (input().split()))
    infos.append((c,a,b))
infos.sort()

ttl_cost = 0
for cost, a, b in infos:
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        ttl_cost += cost
print(ttl_cost)