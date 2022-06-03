# https://www.acmicpc.net/problem/16953

import sys
sys.setrecursionlimit(int(1e6))

A, B = map(int, sys.stdin.readline().rstrip().split())

ans = int(1e9)
def dfs(num, cnt):
    # print(num, cnt)
    global ans
    if num > B:
        return

    elif num == B:
        ans = min(ans, cnt)

    elif num < B:
        dfs(num*2, cnt + 1)
        dfs(int(str(num)+str(1)), cnt + 1)


dfs(A, 1)
if ans == int(1e9):
    ans = -1
print(ans)