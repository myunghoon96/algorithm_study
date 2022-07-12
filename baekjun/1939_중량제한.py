# https://www.acmicpc.net/problem/1939
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

start, end = map(int, sys.stdin.readline().split())


def bfs(w):
    q = deque()
    q.append(start)
    visit = set()
    visit.add(start)

    while q:
        cur = q.popleft()
        if cur == end:
            return True

        for next_weight, next_node in graph[cur]:
            if next_node not in visit and next_weight >= w:
                visit.add(next_node)
                q.append(next_node)

    return False

ans = -1
left, right = 1, 1000000001 
while left <= right:
    mid = (left + right)//2

    if bfs(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)