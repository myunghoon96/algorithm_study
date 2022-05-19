# https://www.acmicpc.net/problem/15900
# pypy3

from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def find_leaf():
    q = deque([[1,0]])
    visit = set([1])
    ttl_dist = 0
    while q:
        pop_node, dist = q.popleft()
        visit.add(pop_node)

        for child_node in graph[pop_node]:
            if child_node not in visit:
                if len(graph[child_node]) == 1 and graph[child_node][0] == pop_node:
                    # print("LEAF ", child_node, dist+1)
                    ttl_dist += (dist+1)
                q.append([child_node, dist+1])
    return ttl_dist
# print(graph)
total_root_to_leaves_distance = find_leaf()

if total_root_to_leaves_distance % 2 == 0:
    print("No")
else:
    print("Yes")