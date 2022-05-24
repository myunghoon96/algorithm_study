# https://www.acmicpc.net/problem/3665
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    last_year = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    changed = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    impossible_flag = False
    ambiguous_flag = False
    for i in range(N-1):
        graph[last_year[i]] = last_year[i+1:]
    for i in range(N):   
        indegree[last_year[i]] = i

    for i in range(M):
        a, b = changed[i]
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a]-=1
            graph[a].append(b)
            indegree[b]+=1
        else:
            graph[a].remove(b)
            indegree[b]-=1
            graph[b].append(a)
            indegree[a]+=1

    q = deque([])
    visit = set()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
            visit.add(i)
        if indegree[i] < 0:
            impossible_flag = True
    if len(q) == 0:
        impossible_flag = True

    ans = []
    while q:
        if len(q) > 1:
            ambiguous_flag = True
        node = q.popleft()
        ans.append(node)

        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
                visit.add(next_node)
    
    if impossible_flag or len(visit) < N:
        print("IMPOSSIBLE")
    elif ambiguous_flag:
        print("?")
    elif len(visit) == N:
        print(*ans)