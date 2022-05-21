import sys

# n, m = 2, 15
# moneys = [2, 3]

n, m = 3, 4
moneys = [3, 5, 7]

dp = [sys.maxsize] * (m+1)
dp[0] = 0
for money in moneys:
    # if money <= m:
    #     dp[money] = 1
    for i in range(money, m+1):
        if dp[i-money] != sys.maxsize:
            dp[i] = min(dp[i], dp[i-money] + 1)

if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])