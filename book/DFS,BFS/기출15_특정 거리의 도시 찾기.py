#https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
start = x

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

visit = [False]*(n+1)
visit[start] = True

ans = []
q = deque([(start, 0)])
while q:
    city, dist = q.popleft()
    visit[city] = True
    # print(city, dist)
    if dist == k:
        ans.append(city)

    for next_city in graph[city]:
        if not visit[next_city]:
            q.append((next_city, dist+1))
            visit[next_city] = True

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for e in ans:
        print(e)