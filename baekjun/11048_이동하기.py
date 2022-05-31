# https://www.acmicpc.net/problem/11048
import copy

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
dp = copy.deepcopy(matrix)

for y in range(M):
    for x in range(N):

        if x-1 >= 0:
            dp[x][y] = max(dp[x][y], matrix[x][y] + dp[x-1][y])
        if y - 1 >= 0:
            dp[x][y] = max(dp[x][y], matrix[x][y] + dp[x][y-1])
        if x - 1 >= 0 and y - 1 >= 0:
            dp[x][y] = max(dp[x][y], matrix[x][y] + dp[x-1][y-1])

print(dp[N-1][M-1])