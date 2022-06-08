# https://www.acmicpc.net/problem/11066
import sys

T = int(input().rstrip())
for _ in range(T):
    K = int(input().rstrip())
    pages = list(map(int, input().split()))
    pre_sum = [0]*(K+1)
    for i in range(len(pages)):
        pre_sum[i+1] = pre_sum[i] + pages[i]

    dp = [[0]*K for _ in range(K)]

    for d in range(1, K):
        for i in range(K-d):
            j = i + d
            dp[i][j] = int(1e9)
            for m in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j] + pre_sum[j+1]-pre_sum[i]) 
            # print((i,j), dp[i][j], pre_sum[j+1]-pre_sum[i])
      
    print(dp[0][-1])