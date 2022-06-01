# https://www.acmicpc.net/problem/1238
from pickletools import dis
import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distances = [[int(1e9)]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))

def dijkstra(start):
    distance = [int(1e9)] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, city = heapq.heappop(q)

        if dist > distance[city]:
            continue

        for next_dist, next_city in graph[city]:
            if dist + next_dist < distance[next_city]:
                distance[next_city] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next_city))

    return distance

for i in range(1, N+1):
    distances[i] = dijkstra(i)

max_time = -1
for i in range(1, N+1):
    max_time = max(max_time, distances[i][X] + distances[X][i])

print(max_time)

