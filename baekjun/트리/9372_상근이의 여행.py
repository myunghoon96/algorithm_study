# https://www.acmicpc.net/problem/9372
#pypy3

from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visit = [False] * (n+1)
    def dfs(place, cnt):
        visit[place] = True
        for next_place in graph[place]:
            if not visit[next_place]:
                cnt = dfs(next_place, cnt+1)
        return cnt

    print(dfs(1, 0))