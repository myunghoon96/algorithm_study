N, M = 7, 11
infos = [
    [0,1,7],
    [0,3,5],
    [1,2,8],
    [1,3,9],
    [1,4,7],
    [2,4,5],
    [3,4,15],
    [3,5,6],
    [4,5,8],
    [4,6,9],
    [5,6,11]
]
infos.sort(key = lambda x: x[2])

parents = [i for i in range(N)]

def find(a):

    if a != parents[a]:
        parents[a] = find(parents[a])
    
    return parents[a]

def union(a, b):

    parents_a = find(a)
    parents_b = find(b)

    if parents_a < parents_b:
        parents[parents_b] = parents_a
    else:
        parents[parents_a] = parents_b

min_cost = 0
ttl_cost = 0
for a, b, cost in infos:
    ttl_cost += cost

    if find(a) != find(b):
        print(a,b, parents)
        union(a, b)
        print(a,b, parents)     
        min_cost += cost

# print(ttl_cost, min_cost)
print(ttl_cost - min_cost)