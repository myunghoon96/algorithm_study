n, m = 7,8
infos = [
    [0,1,3],
    [1,1,7],
    [0,7,6],
    [1,7,1],
    [0,3,7],
    [0,4,2],
    [0,1,1],
    [1,1,1],
]

parents = [i for i in range(n+1)]

def union(x,y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent < y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent

    return

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]

for info in infos:
    action, a, b = info
    if action == 0:
        union(a,b)
    elif action == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")