# https://www.acmicpc.net/problem/1167
import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    tmp_input = list(map(int, input().split()))
    a = tmp_input[0]
    for i in range(1, len(tmp_input)-1, 2):
        b, c = tmp_input[i], tmp_input[i+1]
        graph[a].append((c, b))

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