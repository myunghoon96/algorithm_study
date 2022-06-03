# https://www.acmicpc.net/problem/2146
from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, island_no):
    q =deque()
    q.append((x,y))
    visit = set()
    visit.add((x,y))
    matrix[x][y] = island_no

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N and (xx,yy) not in visit and matrix[xx][yy] == 1:
                visit.add((xx,yy))
                q.append((xx,yy))        
                matrix[xx][yy] = island_no

island_no = 2
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            bfs(i, j, island_no)
            island_no += 1


def bfs2(xy_pairs, no):
    q = deque()

    for x, y in xy_pairs:
        q.append((x,y,0))

    visit = set()
    
    min_dist = int(1e9)
    while q:
        x, y, dist = q.popleft()
        if matrix[x][y] != 0 and matrix[x][y] != no:
            min_dist = min(min_dist, dist)
            return min_dist

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N and (xx,yy) not in visit and matrix[xx][yy] != no:
                visit.add((xx,yy))
                q.append((xx,yy, dist+1))
    
            


ans = int(1e9)
for no in range(2, island_no):
    # print("NO ", no)
    xy_pairs = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == no:
                xy_pairs.append((i,j))
    result = bfs2(xy_pairs, no)
    # print("result ", result)
    ans = min(ans, result) 
print(ans-1)   
