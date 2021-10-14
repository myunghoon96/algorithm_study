#https://www.acmicpc.net/problem/14891

import sys
from collections import deque

gear1 = deque([int(e) for e in sys.stdin.readline().strip()])
gear2 = deque([int(e) for e in sys.stdin.readline().strip()])
gear3 = deque([int(e) for e in sys.stdin.readline().strip()]) 
gear4 = deque([int(e) for e in sys.stdin.readline().strip()])
gears =[gear1, gear2, gear3, gear4]
instructions = []
k = int(sys.stdin.readline())
for _ in range(k):
    instructions.append(list(map(int, sys.stdin.readline().split())))

def check_and_rotate(idx, dir):
    need_rotate = [[idx, dir]]

    left_idx, right_idx = idx-1, idx+1
    left_dir, right_dir = -dir, -dir
    while 0<=left_idx<4: # check left
        if gears[left_idx][2] != gears[left_idx+1][6]:
            need_rotate.append([left_idx, left_dir])
            left_idx-=1
            left_dir = -left_dir
        else:
            break

    while 0<=right_idx<4: # check right
            if gears[right_idx-1][2] != gears[right_idx][6]:
                need_rotate.append([right_idx, right_dir])
                right_idx+=1
                right_dir=-right_dir
            else:
                break

    for e in need_rotate:
        idx, dir = e
        gears[idx].rotate(dir)

for ins in instructions:
    idx, dir = ins
    check_and_rotate(idx-1, dir)

ans = 0
for num, gear in enumerate(gears):
    if gear[0]!=0:
        ans+=2**num

print(ans)