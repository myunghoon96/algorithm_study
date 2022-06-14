# https://www.acmicpc.net/problem/6064

import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    stop_flag = False

    ans = x
    while ans <= (M * N):
        if (ans - x) % M == 0 and (ans - y) % N == 0:
            print(ans)
            stop_flag = True
            break
        ans += M

    if not stop_flag:
        print(-1)