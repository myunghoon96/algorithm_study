# https://www.acmicpc.net/problem/1504
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

u, v = map(int, input().split())

def dijkstra(start, end):
    distance = [int(1e9)] * (N+1)
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for next_dist, next_node in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next_node))
    
    return distance[end]

one_to_u = dijkstra(1, u)
one_to_v = dijkstra(1, v)
u_to_v = v_to_u = dijkstra(u, v)
u_to_n = dijkstra(u, N)
v_to_n = dijkstra(v,N)

first_way = one_to_u + u_to_v + v_to_n
second_way = one_to_v + v_to_u + u_to_n

ans = min(first_way, second_way)

if ans >= int(1e9):
    ans = -1
print(ans)