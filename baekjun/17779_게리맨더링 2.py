#https://www.acmicpc.net/problem/17779

import sys
from collections import deque
n=int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = sys.maxsize

def area(x,y,d1,d2):
    global ans
    if x+d1>=n or y-d1<0 or x+d2>=n or y+d2>=n or x+d1+d2>=n or y-d1+d2>=n or y+d2-d1<0 or y+d2-d1>=n:
        return
    areas=[0]*5
    visit = [[0]*n for _ in range(n)]

    for i in range(0, d1+1): #left up
        visit[x+i][y-i]=5
    for i in range(0, d2+1): #right up
        visit[x+i][y+i]=5
    for i in range(0, d2+1): #left down
        visit[x+d1+i][y-d1+i]=5
    for i in range(0, d1+1): #right down
        visit[x+d2+i][y+d2-i]=5

    # for r in range(n):
    #     if area[r].count(5) < 2 :
    #         continue
    #     five_check = False
    #     cnt = 0
    #     for c in range(n):
    #         if area[r][c] == 5:
    #             five_check = True
    #             cnt += 1
    #             if cnt == 2:
    #                 five_check = False
    #             continue
    #         if five_check:
    #             area[r][c] = 5

    #area 1
    for r in range(x+d1):
        for c in range(y+1):
            if visit[r][c]==5:
                break
            elif visit[r][c]!=5:
                visit[r][c]=1
                areas[0]+=mat[r][c]

    #area 2
    for r in range(x+d2+1):
        for c in range(n-1,y,-1):
            if visit[r][c]==5:
                break
            elif visit[r][c]!=5:
                visit[r][c]=2
                areas[1]+=mat[r][c]
    #area3
    for r in range(x+d1, n):
        for c in range(y-d1+d2):
            if visit[r][c]==5:
                break
            elif visit[r][c]!=5:
                visit[r][c]=3
                areas[2]+=mat[r][c]

    #area4
    for r in range(x+d2+1, n):
        for c in range(n-1, y-d1+d2-1,-1):
            if visit[r][c]==5:
                break
            elif visit[r][c]!=5:
                visit[r][c]=4
                areas[3]+=mat[r][c]

    #area5
    areas[4]=total-sum(areas)
    ans = min(ans,max(areas)-min(areas))



total = 0
for e in mat:
    total+=sum(e)

for i in range(1,n):
    for j in range(1,n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                area(i,j,d1,d2)

print(ans)