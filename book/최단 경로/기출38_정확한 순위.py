from collections import deque

N, M = 6, 6
infos = [
    [1,5],
    [3,4],
    [4,2],
    [4,6],
    [5,2],
    [5,4],
]

graph =[[int(1e9)]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for x, y in infos:
    graph[x][y] = 1

for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
            cnt += 1
    if cnt == N:
        ans += 1
print(ans)
# indegree = [0] * (N+1)

# for info in infos:
#     a, b = info
#     graph[a].append(b)
#     indegree[b] += 1

# q = deque()
# for i in range(1, N+1):
#     if indegree[i] == 0:
#         q.append(i)

# while q:
#     node = q.popleft()
#     print('node', node)
#     for next_node in graph[node]:
#         indegree[next_node] -= 1
#         if indegree[next_node] == 0:
#             print('next_node', next_node)
#             q.append(next_node)