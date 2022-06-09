# https://www.acmicpc.net/problem/2133

N = int(input())

if N % 2 == 1:
    print(0)
    exit()

dp = [0] * (N+1)
dp[2] = 3

for i in range(4,N+1,2):
    for j in range(2, i, 2):
        # print(i, j, i-j)
        if j == 2:
            dp[i] += (dp[i-j] * 3)
        else:
            dp[i] += (dp[i-j] * 2)
    dp[i] += 2

# print(dp)
print(dp[N])


