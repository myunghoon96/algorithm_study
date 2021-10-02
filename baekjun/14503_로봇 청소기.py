#https://www.acmicpc.net/problem/14503
import sys
from collections import deque

def mov(x,y,d, matrix, row, col):
    ans = 0
    d_list = [3, 0, 1, 2]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q=deque()
    q.append((x,y,d))

    matrix[x][y]=2
    ans+=1

    while q:
        x,y,d = q.popleft()
        nd = d
        status = False
        for i in range(4):
            nd = d_list[nd]
            nx, ny = x+dx[nd], y+dy[nd]
            if 0<=nx<row and 0<=ny<col and matrix[nx][ny]==0:
                q.append((nx,ny,nd))
                matrix[nx][ny]=2
                ans+=1
                status = True
                break
            
        if status == False:
            bx, by = x-dx[d], y-dy[d]
            if 0<=bx<row and 0<=by<col and matrix[bx][by]!=1:
                q.append((bx,by,d))

            elif 0<=bx<row and 0<=by<col and matrix[bx][by]==1:
                # print("FINISH", ans, x,y)
                return ans
            
    return

row, col = map(int, sys.stdin.readline().split())

cur_x, cur_y, cur_d = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(row):
    temp=list(map(int,(sys.stdin.readline().split())))
    matrix.append(temp)

# for r in matrix:
#     print(r)

ans = mov(cur_x, cur_y, cur_d, matrix, row, col)

# for r in matrix:
#     print(r)

print(ans)
