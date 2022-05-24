# https://www.acmicpc.net/problem/18353

N = int(input())
people = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if people[i] < people[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(N - max(dp))