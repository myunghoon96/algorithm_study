# https://www.acmicpc.net/problem/1922
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
infos = [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)]

def find_parent(a):

    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    
    return parents[a]

def union(a, b):

    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a < parent_b:
        parents[parent_b] = parent_a
    elif parent_a > parent_b:
        parents[parent_a] = parent_b

ttl_cost = 0
infos.sort(key= lambda x: (x[2], x[0], x[1]))
for a, b, c in infos:
    if find_parent(a) != find_parent(b):
        union(a, b)
        ttl_cost += c

print(ttl_cost)