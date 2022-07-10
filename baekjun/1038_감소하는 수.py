# https://www.acmicpc.net/problem/1038
import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())

all_decreasing_nums = []
#longest 9876543210, 10자리 수
for i in range(1, 11):
    combis = list(combinations([e for e in range(0, 10)], i))
    for combi in combis:
        str_num = ''.join(map(str, sorted(combi, reverse=True)))
        all_decreasing_nums.append(int(str_num))

all_decreasing_nums.sort()
if N < len(all_decreasing_nums):
    print(all_decreasing_nums[N])
else:
    print(-1)