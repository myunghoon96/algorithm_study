# https://www.acmicpc.net/problem/20055
from collections import deque
from hashlib import new
import sys

N, K = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))
robots = deque([0] * N)
ans = 0

while True:
    #1
    belt.rotate(1)
    robots.rotate(1)
    robots[-1] = 0

    #2
    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and belt[i+1] > 0:
            robots[i+1] = 1
            robots[i] = 0 
            belt[i+1] -= 1
    robots[-1] = 0

    #3
    if belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1


    ans += 1
    #4
    zero_cnt = belt.count(0)
    if zero_cnt >= K:
        break


print(ans)

