# n, m = 5, 7
# infos = [
#     [1,2],
#     [1,3],
#     [1,4],
#     [2,4],
#     [3,4],
#     [3,5],
#     [4,5],
# ]
# x, k = 4, 5

n, m = 4, 2
infos = [
    [1,3],
    [2,4]
]
x, k = 3, 4

graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
for info in infos:
    a,b = info
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# for e in graph:
#     print(e)

if graph[1][k] + graph[k][x] >= int(1e9):
    print(-1)
else:
    print(graph[1][k] + graph[k][x])