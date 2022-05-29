# https://www.acmicpc.net/problem/1916
import heapq
import sys


input = sys.stdin.readline

N = int(input())
M = int(input())
q = []
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    
start, end = map(int, input().split())

distances = [sys.maxsize for i in range(N+1)]
q.append((0, start))

while q:
    cost, a = heapq.heappop(q)

    if cost > distances[a]:
        continue
    #메모리 초과 원인
    #다익스트라 주의
    # distances[a] = cost
    if a == end:
        break

    for next_cost, next_city in graph[a]:
        if cost + next_cost < distances[next_city]:
            #메모리 초과 해결
            distances[next_city] = cost + next_cost
            heapq.heappush(q, (cost + next_cost, next_city))

# print(distances)
print(distances[end])