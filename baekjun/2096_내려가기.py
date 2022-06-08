# https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    a, b, c = map(int, input().split())
    cur_dp = [a,b,c]
    cur_dp2 = [a,b,c]
    if i == 0:
        pre_dp = [a,b,c]
        pre_dp2 = [a,b,c]
        continue

    cur_dp[0] += max(pre_dp[0], pre_dp[1])
    cur_dp2[0] += min(pre_dp2[0], pre_dp2[1])

    cur_dp[1] += max(max(pre_dp[0], pre_dp[1]), pre_dp[2])
    cur_dp2[1] += min(min(pre_dp2[0], pre_dp2[1]),pre_dp2[2])

    cur_dp[2] += max(pre_dp[1], pre_dp[2])
    cur_dp2[2] += min(pre_dp2[1], pre_dp2[2])

    # print(i, cur_dp2)
    pre_dp = cur_dp
    pre_dp2 = cur_dp2
# print(cur_dp, cur_dp2)
print(max(cur_dp), min(cur_dp2))
