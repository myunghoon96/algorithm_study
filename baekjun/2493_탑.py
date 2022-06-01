# https://www.acmicpc.net/problem/2493

import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = [(N-1, towers[-1])]
ans = [0] * N

for i in range(N-2, -1, -1):
    cur_tower = towers[i]
    # print(i, cur_tower)
    if stack:
        while stack:
            pre_last_idx, pre_last_tower = stack[-1]
            if pre_last_tower <= cur_tower:
                stack.pop()
                ans[pre_last_idx] = i + 1
            else:
                break

    stack.append((i, cur_tower))

print(*ans)