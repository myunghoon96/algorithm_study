#https://www.acmicpc.net/problem/9470

import sys
from collections import deque
input = sys.stdin.readline

t=int(input())
for test_num in range(1,t+1):
    k,m,p = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(p)]

    graph = [[] for _ in range(m+1)]
    degree = [0]*(m+1)
    for info in infos:
        a,b = info
        graph[a].append(b)
        degree[b]+=1

    q=deque()
    level_cnt = [[0,0] for _ in range(m+1)]
    for i in range(1, m+1):
        if degree[i]==0:
            q.append(i)
            level_cnt[i] = [1,1]


    while q:
        cur = q.popleft()

        if level_cnt[cur][1] >= 2:
            level_cnt[cur] = [level_cnt[cur][0]+1, 1]

        cur_level, cur_cnt = level_cnt[cur]
        for next in graph[cur]:
            degree[next]-=1
            next_level, next_cnt = level_cnt[next]
            if cur_level==next_level:
                level_cnt[next] = [next_level, next_cnt+1]
            else:
                if cur_level<next_level:
                    pass
                elif cur_level>next_level:
                    level_cnt[next] = [cur_level, 1]
            if degree[next]==0:
                q.append(next)

    levels = [e[0] for e in level_cnt]
    print(k, end=" ")
    print(max(levels))