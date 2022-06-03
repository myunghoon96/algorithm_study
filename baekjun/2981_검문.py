# https://www.acmicpc.net/problem/2981

# A = M * a + remain
# B = M * b + remain
# C = M * c + remain
# B - A = (M*b) - (M*a) = M * (b-a)
# C - B = (M*c) - (M*b) = M * (c-b)

import sys
import math

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
nums.sort()

nums_diff = [nums[i] - nums[i-1] for i in range(1,N)]
tmp_gcd = nums_diff[0]

for i in range(1, N-1):
    tmp_gcd = math.gcd(tmp_gcd, nums_diff[i])

ans = set()
for i in range(1, int(tmp_gcd**0.5)+1):
    if tmp_gcd % i == 0:
        ans.add(i)
        ans.add(tmp_gcd//i)
ans.remove(1)
ans = sorted(list(ans))

print(*ans)