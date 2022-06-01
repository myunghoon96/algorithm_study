# https://www.acmicpc.net/problem/1261
from collections import deque
import sys
#0-1 bfs, appendleft

input = sys.stdin.readline

M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0))
    visit = set()
    visit.add((0,0,0))

    while q:
        x, y, cnt = q.popleft()
        if x == N-1 and y == M-1:
            print(cnt)
            return

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < N and 0 <= yy < M and (xx, yy) not in visit:
                visit.add((xx,yy))
                if matrix[xx][yy] == 0: 
                    q.appendleft((xx, yy, cnt))
                elif matrix[xx][yy] == 1:
                    q.append((xx, yy, cnt + 1))
                
    return

bfs()
