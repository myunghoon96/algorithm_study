# https://www.acmicpc.net/problem/1068
from calendar import c
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
del_node = int(input().rstrip())

graph = [[] for _ in range(N)]
root = -1
for child, parent in enumerate(parents):
    if parent == -1:
        root = child
        continue
    graph[parent].append(child)

ans = 0
def bfs():
    global ans

    q = deque([])
    if root != del_node:
        q.append(root)
    else:
        return
    visit = set()
    visit.add(root)

    while q:
        cur_node = q.popleft()
        # print('cur_node ',cur_node)

        if len(graph[cur_node]) == 0:
            ans += 1
            continue
        
        if len(graph[cur_node]) == 1 and graph[cur_node][0] == del_node:
            ans += 1
            continue

        for child_node in graph[cur_node]:
            if child_node == del_node:
                continue
            if child_node not in visit:
                visit.add(child_node)
                q.append(child_node)
    
bfs()
print(ans)