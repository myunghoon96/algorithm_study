N, M = 5, 4
matrix = [
    [0,1,0,1,1],
    [1,0,1,1,0],
    [0,1,0,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0],
]
plan = [2,3,4,3]
parents = [i for i in range(N+1)]
def find(a):

    if a != parents[a]:
        parents[a] = find(parents[a])
    
    return parents[a]

def union(a, b):

    parents_a = find(a)
    parents_b = find(b)

    if parents_a <= parents_b:
        parents[parents_b] = parents_a
    else:
        parents[parents_a] = parents_b

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            a, b = i+1, j+1
            if find(a) != find(b):
                union(a,b)

print(parents)
parents_set = set()
for e in plan:
    parents_set.add(parents[e])
if len(parents_set) == 1:
    print("YES")
else:
    print("NO")