# https://www.acmicpc.net/problem/1865
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []
    distances = [int(1e9) for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T))
    
    # bellman ford
    def bf(start_node):
        distances[start_node] = 0

        for i in range(N):
            for edge in edges:
                cur_node, next_node, cost = edge

                # if distances[cur_node] != int(1e9) and distances[cur_node] + cost < distances[next_node]:
                if distances[cur_node] + cost < distances[next_node]:
                    distances[next_node] = distances[cur_node] + cost

                    if i == N-1:
                        return True

        return False
    
    result = bf(1)

    if result:
        print("YES")
    else:
        print("NO")