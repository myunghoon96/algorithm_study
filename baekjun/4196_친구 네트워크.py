# https://www.acmicpc.net/problem/4195
from gettext import find
import numbers
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input().rstrip())

def find_parent(parents, x):
    if parents[x] != x :
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, x, y, cnt):
    x = find_parent(parents, x)
    y = find_parent(parents, y)

    if x < y:
        parents[y] = x
        cnt[x] += cnt[y]
    elif x > y:
        parents[x] = y
        cnt[y] += cnt[x]
for _ in range(T):
    parents = defaultdict(str)
    cnt = defaultdict(int)

    F = int(input().rstrip())
    for _ in range(F):
        a, b = input().split()
        if a not in parents.keys():
            parents[a] = a
            cnt[a] = 1
        if b not in parents.keys():
            parents[b] = b
            cnt[b] = 1

        union(parents, a, b, cnt)        
        # find_parent(parents, a)
        # find_parent(parents, b)

        print(cnt[find_parent(parents, a)])
        # print(parents)


