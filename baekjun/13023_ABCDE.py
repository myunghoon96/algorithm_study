# https://www.acmicpc.net/problem/13023
import sys
from collections import deque

sys.setrecursionlimit(int(10e6))

N, M = map(int, (sys.stdin.readline().split()))
graph = [[] for _ in range(N)]
ans = 0
visit = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, (sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, cnt):
    global ans
    if cnt == 4:
        ans = 1
        return
    
    for next_node in graph[x]:
        if not visit[next_node]:
            visit[next_node] = True
            dfs(next_node, cnt + 1)
            visit[next_node] = False
    return

for i in range(N):
    visit[i] = True
    dfs(i, 0)
    visit[i] = False
    
    if ans == 1:
        break

print(ans)