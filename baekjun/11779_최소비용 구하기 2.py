# https://www.acmicpc.net/problem/11779

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0
    history = [-1] * (N + 1)
    
    while q:
        cost, city = heapq.heappop(q)
        if cost > distances[city]:
            continue
        
        for next_cost, next_city in graph[city]:
            if cost + next_cost < distances[next_city]:
                distances[next_city] = cost + next_cost
                heapq.heappush(q, (cost + next_cost, next_city))
                history[next_city] = city

    # print(distances)
    print(distances[end])
    # print(history)

    path = []
    city = end
    while True:
        if history[city] == -1:
            break
        path.append(city)
        city = history[city]
    path.append(start)
    print(len(path))
    print(" ".join(map(str, path[::-1])))

dijkstra(start)