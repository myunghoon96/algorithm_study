# T = 2
N, M = 3, 4
golds = [1,3,3,2,2,1,4,1,0,6,4,7]

N, M = 4, 4
golds = [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]
row, col = N, M
matrix = [[0]*(M+2) for _ in range(N+2)]
idx = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        matrix[i][j] = golds[idx]
        idx += 1


ans = 0
#  i j 순서 중요
for j in range(1,M+1):
    for i in range(1,N+1):
        matrix[i][j] = matrix[i][j] + max(matrix[i][j-1], matrix[i-1][j-1], matrix[i+1][j-1])
        ans = max(ans, matrix[i][j])

# for e in matrix:
#     print(e)

print(ans)