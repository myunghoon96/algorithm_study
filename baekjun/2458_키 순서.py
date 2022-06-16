# https://www.acmicpc.net/problem/2458

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distances = [[int(1e9)]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    distances[i][i] = 0

def dijkstra(start):
    global distances

    q = []
    heapq.heappush(q, (0, start))
    distances[start][start] = 0

    while q:
        dist, student = heapq.heappop(q)
        # print(dist, student)
        for next_student in graph[student]:
            next_dist = 1
            if dist + next_dist < distances[start][next_student]:
                heapq.heappush(q, (dist + next_dist, next_student))
                distances[start][next_student] = dist + next_dist

for i in range(1, N+1):
    dijkstra(i)

ans = 0
for i in range(1, N+1):
    tall_student_cnt = 0
    short_student_cnt = 0
    for j in range(1, N+1):
        if i != j and distances[i][j] != int(1e9):
            tall_student_cnt += 1
    
    for k in range(1, N+1):
        if i != k and distances[k][i] != int(1e9):
            short_student_cnt += 1

    if tall_student_cnt + short_student_cnt == N - 1:
        ans += 1    

print(ans)
