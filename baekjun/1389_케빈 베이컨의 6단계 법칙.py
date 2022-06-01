# https://www.acmicpc.net/problem/1389

N, M = map(int, input().split())
distances = [[int(1e9)]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    distances[a][b] = 1
    distances[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

min_person = -1
min_sum = int(1e9)
for person, dists in enumerate(distances):
    if person == 0: 
        continue
    # print(person, sum(dists[1:]))

    if sum(dists[1:]) < min_sum:
        min_sum = sum(dists[1:])
        min_person = person

print(min_person)