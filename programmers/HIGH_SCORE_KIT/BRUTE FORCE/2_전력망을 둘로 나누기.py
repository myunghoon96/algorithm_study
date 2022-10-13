# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from itertools import combinations
from collections import deque


def solution(n, wires):
    answer = n + 1
    remain_wires_combis = list(combinations(wires, n-2))

    def bfs(start, visit):
        q = deque()
        q.append(start)
        cnt = 0

        while q:
            node = q.popleft()
            cnt += 1
            for next_node in graph[node]:
                if next_node not in visit:
                    visit.add(next_node)
                    q.append(next_node)
        return cnt

    for remain_wires in remain_wires_combis:
        graph = [[] for _ in range(n+1)]
        visit = set()

        for wire in remain_wires:
            a, b = wire
            graph[a].append(b)
            graph[b].append(a)

        for start in range(1, n + 1):
            if start not in visit:
                visit.add(start)
                cnt = bfs(start, visit)
                diff = abs(cnt - (n - cnt))
                answer = min(answer, diff)
                break

    return answer
