# https://www.acmicpc.net/problem/9205
from collections import deque
import sys

input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(infos):
    home = infos[0]
    q = deque([])
    q.append((home[0], home[1]))
    visit =set()
    visit.add((home[0], home[1]))
    rock = infos[-1]

    while q:
        x, y = q.popleft()
        # print("@@", (x,y), rock)
        if (x, y) == rock:
            return True
        for place_x, place_y in infos[1:]:
            if (place_x, place_y) not in visit and distance(x, y, place_x, place_y) <= 20 * 50:
                q.append((place_x, place_y))
                visit.add((place_x, place_y))
    return False

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    infos = [tuple(map(int, (input().rstrip().split()))) for _ in range(N+2)]

    result = bfs(infos)

    if result:
        print("happy")
    else:
        print("sad")
