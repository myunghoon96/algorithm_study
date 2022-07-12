# https://www.acmicpc.net/problem/16928
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dic = dict()

for _ in range(N + M):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] = b

def bfs():
    q = deque()
    q.append((1,0))
    visit = [-1] * 101
    visit[0] = 0

    while q:
        cur, cnt = q.popleft()

        if cur == 100:
            print(cnt)
            return

        for i in range(1, 7):
            next = cur + i
            if next > 100:
                continue

            if visit[next] != -1:
                continue

            if next in dic.keys():
                next = dic[next]

            if visit[next] == -1:
                visit[next] = cnt + 1
                q.append((next, cnt + 1))
    return

bfs()