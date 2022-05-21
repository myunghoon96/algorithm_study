from collections import deque

n, m = 5, 6
matrix = [
[1,0,1,0,1,0],
[1,1,1,1,1,1],
[0,0,0,0,0,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1]]

visit = [[False]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    q = deque([(0,0,1)])
    visit[0][0] = True

    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and matrix[xx][yy] == 1 and not visit[xx][yy]:
                visit[xx][yy] = True
                q.append((xx,yy,cnt+1))

ans = bfs()
print(ans)