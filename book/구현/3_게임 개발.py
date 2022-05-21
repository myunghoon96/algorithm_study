n, m = 4, 4
x, y, direc = 1, 1, 0
matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

visit = [[False] * m for _ in range(n)]
visit[x][y] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

tmp_cnt = 0
ans = 1
while True:
    # 1
    direc = (direc-1) % 4

    # 2
    if tmp_cnt <= 3:
        xx = x + dx[direc]
        yy = y + dy[direc]
        if 0 <= xx < n and 0 <= yy < m and not visit[xx][yy] and matrix[xx][yy] == 0:
            x, y = xx, yy
            visit[xx][yy] = True
            ans += 1
            tmp_cnt = 0
        else:
            tmp_cnt += 1
            continue

    # 3
    elif tmp_cnt >= 4:
        rev_direc = (direc+2)%4
        xx = x + dx[rev_direc]
        yy = y + dy[rev_direc]
        
        if 0 <= xx < n and 0 <= yy < m and not visit[xx][yy] and matrix[xx][yy] == 0:
            x, y = xx, yy
            visit[xx][yy] = True
            ans += 1
        else:
            break
        tmp_cnt = 0

# for r in visit:
#     print(r)
    
print(ans)