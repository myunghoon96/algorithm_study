from re import X


n, m = 7, 12
infos =[
    [1,2,3],
    [1,3,2],
    [3,2,1],
    [2,5,2],
    [3,4,4],
    [7,3,6],
    [5,1,5],
    [1,6,2],
    [6,4,1],
    [6,5,3],
    [4,5,3],
    [6,7,4],
]

parents = [i for i in range(n+1)]

def union(x,y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent < y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent

def find(x):

    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

ttl_cost = 0
max_cost = -1
#sort by cost asc
infos = sorted(infos, key= lambda x:x[2])

for info in infos:
    a, b, cost = info
    if find(a) != find(b):
        union(a,b)
        max_cost = max(max_cost, cost)
        ttl_cost += cost
        # print(a,b, cost, ttl_cost)

print(ttl_cost - max_cost)