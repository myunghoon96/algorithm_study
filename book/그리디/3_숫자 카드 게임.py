n, m = 2, 4
matrix = [[7,3,1,8], [3,3,3,4]]

ans = -1
for row in matrix:
    ans = max(ans, min(row))

print(ans)
