# https://www.acmicpc.net/problem/12852
import sys

N = int(sys.stdin.readline())
dp = [N+1 for _ in range(N+1)]
history = [[num] for num in range(N+1)]
dp[1] = 0

for num in range(2, N+1):
    dp[num] = dp[num-1] + 1
    history[num] = history[num-1] + [num]

    if num % 3 == 0 and dp[num] > dp[num//3] + 1:
        dp[num] = dp[num//3] + 1
        history[num] = history[num//3] + [num]

    if num % 2 == 0 and dp[num] > dp[num//2] + 1:
        dp[num] = dp[num//2] + 1
        history[num] = history[num//2] + [num]


print(dp[N])
print(' '.join(map(str, history[N][::-1])))