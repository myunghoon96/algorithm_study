# https://www.acmicpc.net/problem/2011

import sys

password = sys.stdin.readline().rstrip()

if int(password[0]) == 0:
    print(0)
    exit()

dp = [0] * len(password)
dp[0] = 1

for i in range(1, len(password)):

    if int(password[i]) > 0:
        dp[i] = dp[i-1]

    if 10 <= int(password[i-1]) * 10 + int(password[i]) <= 26:
        if i == 1:
            dp[i] += 1
        else:
            dp[i] += dp[i-2]

    dp[i] %= 1000000

print(dp[-1])
