# https://www.acmicpc.net/problem/9019

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    def bfs(cur):
        q = deque()
        q.append((cur, ""))
        visit = set()
        visit.add(cur)

        while q:
            cur, history = q.popleft()
            if cur == B:
                print(history)
                break

            num_d = (2*cur)%10000
            if num_d not in visit:
                q.append(((2*cur)%10000, history+"D"))
                visit.add(num_d)

            num_s = (cur-1)%10000
            if  num_s not in visit:
                q.append((num_s, history+"S"))
                visit.add(num_s)

            front, rest = cur//1000, cur%1000
            num_l = rest*10 + front
            # cur_str = str(cur).zfill(4)
            # d1, d2, d3, d4 = cur_str[0], cur_str[1], cur_str[2], cur_str[3]
            # num_l = int(d2+d3+d4+d1)
            if  num_l not in visit:
                q.append((num_l, history+"L"))
                visit.add(num_l)

            last, rest = cur%10, cur//10
            num_r = last*1000 + rest 
            # num_r = int(d4+d1+d2+d3)               
            if num_r not in visit:
                q.append((num_r, history+"R"))
                visit.add(num_r)

    bfs(A)
