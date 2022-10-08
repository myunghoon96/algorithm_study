# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs():
        q = deque([(0, 0, 1)])
        visit = set([(0, 0)])

        while q:
            x, y, dist = q.popleft()
            if x == len(maps) - 1 and y == len(maps[0]) - 1:
                return dist

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if 0 <= xx < len(maps) and 0 <= yy < len(maps[0]) and (xx, yy) not in visit and maps[xx][yy] == 1:
                    visit.add((xx, yy))
                    q.append((xx, yy, dist + 1))

        return -1

    answer = bfs()

    return answer
