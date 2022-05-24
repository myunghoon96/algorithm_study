# https://www.acmicpc.net/problem/18405
from collections import defaultdict, deque


n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

q = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((matrix[i][j],i,j,0))

q.sort()

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(q):
    q = deque(q)
    while q :        
        virus, a, b, time = q.popleft()
        # print(virus, a, b, time)
        if time == s:
            return 

        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]

            if 0 <= xx < n and 0 <= yy < n and matrix[xx][yy] == 0:
                matrix[xx][yy] = virus
                q.append((virus, xx, yy, time + 1))
    return

bfs(q)
# print("@@@@@@")
# for e in matrix:
#     print(e)

print(matrix[x-1][y-1])