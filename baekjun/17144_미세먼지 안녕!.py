#https://www.acmicpc.net/problem/17144
from functools import partial
import sys
r, c, t = map(int, sys.stdin.readline().split())
mat = [ list(map(int, sys.stdin.readline().split())) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
machines = []

for i in range(r):
    for j in range(c):
        if mat[i][j]==-1:
            machines.append((i,j))
    
def expand():
    global mat
    new_mat = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if (x,y) in machines:
                continue
            if mat[x][y] <5:
                continue
            part = mat[x][y]//5
            for i in range(4):
                xx, yy = x+dx[i], y+dy[i]
                if 0<=xx<r and 0<=yy<c and mat[xx][yy]!=-1:
                    new_mat[xx][yy]+=part
                    new_mat[x][y]-=part    

    for i in range(r):
        for j in range(c):
            mat[i][j]+=new_mat[i][j]

def wind_up():
    dx = [0, -1, 0, 1]	# 우, 상, 좌, 하
    dy = [1, 0, -1, 0]
    m1 = machines[0]
    m1_x, m1_y = m1
    cur = mat[m1_x][1]
    mat[m1_x][1] = 0
    i = 0
    x = m1_x
    y = 1
    while True:
        x = x+dx[i]
        y = y+dy[i]
        if x==m1_x and y==m1_y:
            break
        next = mat[x][y]
        mat[x][y] = cur
        cur = next
        
        if x + dx[i] < 0 or x + dx[i] > m1_x or y + dy[i] < 0 or y + dy[i] >= c:
            i += 1
        if i == 4:
            break

def wind_down():
    dx = [0, 1, 0, -1]	# 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
								
    m2 = machines[1]
    m2_x, m2_y = m2
    cur = mat[m2_x][1]
    mat[m2_x][1] = 0
    i = 0
    x = m2_x
    y = 1
    while True:
        x = x+dx[i]
        y = y+dy[i]
        if x==m2_x and y==m2_y:
            break
        next = mat[x][y]
        mat[x][y] = cur
        cur = next
        
        if x + dx[i] < m2_x or x + dx[i] >= r or y + dy[i] < 0 or y + dy[i] >= c:
            i += 1
        if i == 4:
            break

for _ in range(t):
    expand()
    wind_up()
    wind_down()

ans = 0
for i in range(r):
    for j in range(c):
        ans+=mat[i][j]

print(ans+2)