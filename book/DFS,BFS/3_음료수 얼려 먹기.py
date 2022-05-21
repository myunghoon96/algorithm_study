from collections import deque

n, m = 4, 5
matrix = [[0,0,1,1,0],
[0,0,0,1,1],
[1,1,1,1,1],
[0,0,0,0,0]]

visit = [[False]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    q = deque([(x,y)])
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and not visit[xx][yy] and matrix[xx][yy] == 0:
                q.append((xx,yy))
                visit[xx][yy] = True

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not visit[i][j]:
            bfs(i, j)
            ans += 1
print(ans)

