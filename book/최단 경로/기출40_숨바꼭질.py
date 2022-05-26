import heapq
from bisect import bisect_left, bisect_right

N, M = 6, 7
infos = [
    [3,6],
    [4,3],
    [3,2],
    [1,3],
    [1,2],
    [2,4],
    [5,2],
]
graph = [[] * (N+1) for _ in range(N+1)]
for info in infos:
    a, b = info
    graph[a].append(b)
    graph[b].append(a)

distances = [int(1e9)] * (N+1)
q = [(0, 1)]

max_dist = -1

while q:
    dist, x = heapq.heappop(q)

    if dist > distances[x]:
        continue
    distances[x] = dist
    max_dist = max(max_dist, dist)

    for next_place in graph[x]:
        heapq.heappush(q, (dist+1, next_place))


print(bisect_left(distances, max_dist), max_dist, bisect_right(distances, max_dist) - bisect_left(distances, max_dist))
