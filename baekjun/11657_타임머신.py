# https://www.acmicpc.net/problem/11657
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c))

distances = [int(1e9) for _ in range(N)]
#bellman_ford 벨만 포드
def has_negative_cycle ():
    distances[0] = 0

    for time in range(N):
        for node in range(N):
            #
            if distances[node] == int(1e9):
                continue
            for next_node, next_cost in graph[node]:
                next_cost += distances[node]
                if distances[next_node] > next_cost:
                    distances[next_node] = next_cost

                    if time == N-1:
                        # print('negative cycle exist')
                        return True
    return False

if has_negative_cycle():
    print(-1)
else:
    for i in range(1,N):
        if distances[i] == int(1e9):
            print(-1)
        else:
            print(distances[i]) 
    
