import sys

x = 26

dp = [0] * (x+1)

dp[1] = 0
for i in range(2, x+1):

    dp[i] = dp[i-1] + 1

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[x])

# ans = sys.maxsize
# dp = [sys.maxsize] * (x+1)
# def dfs(num, cnt):
#     global ans

#     print(num, cnt)
#     if num == 1:
#         ans = min(ans, cnt)        
#     if num % 5 == 0:
#         dfs(num//5, cnt+1)
#     if num % 3 == 0:
#         dfs(num//3, cnt+1)
#     if num % 2 == 0:
#         dfs(num//2, cnt+1)
#     if num > 1:
#         dfs(num-1, cnt+1)

# dfs(x, 0)
# print(ans)