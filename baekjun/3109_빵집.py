# https://www.acmicpc.net/problem/3109

import sys

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

def dfs(i, j):
    if j == C-1:
        return True
    
    # moves = [(0, 1), (-1, 1), (1, 1)]
    moves = [(-1, 1), (0, 1), (1, 1)]
    for move in moves:
        xx = i + move[0]
        yy = j + move[1]
        if 0 <= xx < R and 0 <= yy < C and matrix[xx][yy] == '.':
            matrix[xx][yy] = 'x'
            if dfs(xx, yy):
                return True

    return False

ans = 0
for i in range(R):
    if dfs(i, 0):
        ans += 1

print(ans)