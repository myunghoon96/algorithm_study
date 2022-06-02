# https://www.acmicpc.net/problem/1967
# bfs 2번, 첫 bfs는 루트에서 제일 먼 노드 찾기, 
# 두번째 bfs는 루트에서 제일 먼 노드와 가장 먼 노드 
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def bfs(start):
    visit = set()
    q = deque([(0, start)])
    visit.add(start)
    max_dist = -1
    max_node = -1

    while q:
        dist, node = q.popleft()

        if dist > max_dist:
            max_dist = dist
            max_node = node

        for next_dist, next_node in graph[node]:
            if next_node not in visit:
                visit.add(next_node)
                q.append((dist+next_dist, next_node))


    return (max_dist, max_node)

dist, node = bfs(1)
dist2, node2 = bfs(node)
print(dist2)