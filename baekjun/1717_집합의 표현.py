# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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


N, M = map(int, input().split())
parents = [i for i in range(N+1)]

for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union(parents, a,b)
    elif oper == 1:
        if find_parent(parents, a) == find_parent(parents, b):
            print("YES")
        else:
            print("NO")
