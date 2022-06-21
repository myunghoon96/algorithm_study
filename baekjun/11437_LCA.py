# https://www.acmicpc.net/problem/11437
# 최소 공통 조상
# pypy3
# recursionlimit 10**6 메모리 초과
import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline().rstrip())
depth = [-1 for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
parents = [-1 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, d):
    if node > N or node <= 0:
        return
    depth[node] = d

    for next_node in graph[node]:
        if not visit[next_node]:
            visit[next_node] = True
            parents[next_node] = node
            dfs(next_node, d + 1)
    return

def lca(a, b):
    
    while depth[a] != depth[b]:
        if depth[a] < depth[b]:
            b = parents[b]
        elif depth[a] > depth[b]:
            a = parents[a]

    while a != b:
        a = parents[a]
        b = parents[b]

    return a

visit[1] = True
dfs(1, 0)
M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # print('node parent depth', a, parents[a], depth[a])
    # print('node parent depth', b, parents[b], depth[b])
    print(lca(a, b))
