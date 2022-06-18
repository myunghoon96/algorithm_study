# https://www.acmicpc.net/problem/3020

import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

N, H = map(int, sys.stdin.readline().split())
walls = [int(sys.stdin.readline()) for _ in range(N)]
top_walls = [walls[i] for i in range(N) if i%2 == 0]
bottom_walls = [walls[i] for i in range(N) if i%2 == 1]

top_walls.sort()
bottom_walls.sort()
# print(top_walls)
# print(bottom_walls)
dic = defaultdict(int)

for height in range(1, H+1):
    broken = 0

    longer_bottom_walls = len(bottom_walls) - bisect_left(bottom_walls, height)
    broken += longer_bottom_walls
            
    longer_top_walls = len(top_walls) - bisect_right(top_walls, H - height)
    broken += longer_top_walls

    dic[broken] += 1

min_broken = min(dic.keys())
print(min_broken, dic[min_broken])
    