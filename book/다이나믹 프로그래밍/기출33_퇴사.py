# https://www.acmicpc.net/problem/14501

N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]
# N + 1 for last day dp[day + 1]
dp = [0] * (N+1)

for day in range(N-1, -1, -1):
    time, price = jobs[day]

    if day + time > N:
        dp[day] = dp[day+1]
    
    else:
        dp[day] = max(dp[day+1], dp[day+time] + price)

print(dp[0])

