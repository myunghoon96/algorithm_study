import heapq

n, m, c = 3, 2, 1
infos = [[1, 2, 4], [1, 3, 2]]

graph = [[] for _ in range(n+1)]
for info in infos:
    a, b, time = info
    graph[a].append((time, b))
    graph[b].append((time, a))

distances = [int(1e9)] * (n+1)
start = c
distances[start] = 0
q = []
# print(distances)
heapq.heappush(q, (0, start))

while q:
    dist, city = heapq.heappop(q)
    if dist < distances[city]:
        continue

    for cost, next_city in graph[city]:
        if dist + cost < distances[next_city]:
            distances[next_city] = dist + cost
            heapq.heappush(q, (dist+cost, next_city))

# print(distances[1:])

cnt = 0
for e in distances:
    if e != int(1e9) and e != 0:
        cnt += 1

max_time = max(distances[1:])
print(cnt, max_time)