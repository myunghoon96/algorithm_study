# https://www.acmicpc.net/problem/18310

import sys
input = sys.stdin.readline

n = int(input())
homes = list(map(int, input().split()))
homes.sort()

mid_idx = n//2 - 1
mid_idx2 = n//2

tmp_dist = 0
tmp_dist2 = 0
for home in homes:
    tmp_dist += abs(home - homes[mid_idx])
    tmp_dist2 += abs(home - homes[mid_idx2])
# print(tmp_dist, tmp_dist2)
if tmp_dist <= tmp_dist2:
    print(homes[mid_idx])
else:
    print(homes[mid_idx2])