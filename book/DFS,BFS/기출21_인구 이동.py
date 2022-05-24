# https://www.acmicpc.net/problem/16234
from collections import deque

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, b, visit):
    ttl_people = matrix[a][b]
    ttl_cntry = [(a,b)]
    q = deque([(a,b)])
    visit[a][b] = True
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and not visit[xx][yy] and L <= abs(matrix[xx][yy] - matrix[x][y]) <= R:
                visit[xx][yy] = True
                q.append((xx,yy))
                ttl_cntry.append((xx,yy))
                ttl_people += matrix[xx][yy]
                
    if len(ttl_cntry) <= 1:
        return False
    else:
        people_per_cntry = ttl_people // len(ttl_cntry)
        for cntry_x, cntry_y in ttl_cntry:
            matrix[cntry_x][cntry_y] = people_per_cntry

    return True

def one_day():
    visit = [[False]*N for _ in range(N)]
    can_move = False 

    need_change = []
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bfs(i,j,visit):
                    can_move = True    

    return can_move


ans = 0
while True:
    can_move = one_day()
    if can_move:
        ans += 1
    elif not can_move:
        break 

print(ans)