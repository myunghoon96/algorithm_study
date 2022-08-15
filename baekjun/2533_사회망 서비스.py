# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

#dp[node][0] node is not early adapter
#dp[node][1] node is early adapter
dp = [[0,1] for _ in range(N+1)]

visit = [False] * (N+1)
def dfs(root):
    visit[root] = True

    for child in graph[root]:
        if not visit[child]:
            dfs(child)
            dp[root][0] += dp[child][1]
            dp[root][1] += min(dp[child][0], dp[child][1])
    return

dfs(1)
print(min(dp[1]))
