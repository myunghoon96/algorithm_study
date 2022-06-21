# https://programmers.co.kr/learn/courses/30/lessons/92343?language=python3

import copy

def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)

    def dfs(cur_node, sheep, wolf, next_nodes):
        nonlocal answer
        answer = max(answer, sheep)
        # print('cur_node, sheep, wolf, next_nodes', cur_node, sheep, wolf, next_nodes)
        for children in graph[cur_node]:
            next_nodes.add(children)

        for next_node in next_nodes:
            if info[next_node] == 0:
                dfs(next_node, sheep + 1, wolf, next_nodes - {next_node})
            else:
                if sheep > wolf + 1:
                    dfs(next_node, sheep, wolf + 1, next_nodes - {next_node})

        return answer
    
    dfs(0, 1, 0, set())
    return answer