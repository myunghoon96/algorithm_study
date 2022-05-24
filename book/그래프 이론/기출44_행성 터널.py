# https://www.acmicpc.net/problem/2887
import sys
import copy

N = int(sys.stdin.readline().rstrip())
position = [[i] + list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]

x_position = sorted(copy.deepcopy(position), key = lambda x : x[1])
y_position = sorted(copy.deepcopy(position), key = lambda x : x[2])
z_position = sorted(copy.deepcopy(position), key = lambda x : x[3])

edges = []

for i in range(N-1):
    edges.append((x_position[i+1][1] - x_position[i][1], x_position[i][0], x_position[i+1][0]))
    edges.append((y_position[i+1][2] - y_position[i][2], y_position[i][0], y_position[i+1][0]))
    edges.append((z_position[i+1][3] - z_position[i][3], z_position[i][0], z_position[i+1][0]))
    
edges.sort()

parent = [i for i in range(N)]
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a <= parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
    return

ttl_cost = 0
for edge in edges:
    cost, a, b = edge

    if find(a) != find(b):
        union(a,b)
        ttl_cost += cost
print(ttl_cost)