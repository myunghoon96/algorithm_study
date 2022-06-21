# https://www.acmicpc.net/problem/17406

from collections import deque
import copy
import sys
from itertools import permutations

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotations = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

ans = int(1e9)
def rotate(r, c, s, mat):

    for k in range(1, s+1):
        q = deque()
        positions = []
        up, right, down, left = r - k, c + k, r + k, c - k
        for j in range(left, right + 1):
            q.append(mat[up][j])
            positions.append((up, j))
        for i in range(up + 1, down + 1):
            q.append(mat[i][right])
            positions.append((i, right))
        for j in range(right - 1, left - 1, -1):
            q.append(mat[down][j])
            positions.append((down, j))
        for i in range(down - 1, up, -1):
            q.append(mat[i][left])
            positions.append((i, left))

        last = q.pop()
        q.appendleft(last)

        for i, (x, y) in enumerate(positions):
            mat[x][y] = q[i] 
        
    return mat

def process(ops, mat):
    global ans
    for op in ops:
        r, c, s = rotations[op]
        # print('r c s', r, c, s)
        mat = rotate(r - 1, c - 1, s, mat)
        # for e in mat:
        #     print(e)
        # print()

    tmp_ans = int(1e9)
    for row in mat:
        tmp_ans = min(tmp_ans, sum(row))
    
    ans = min(ans, tmp_ans)
    return

permus = permutations([i for i in range(len(rotations))], len(rotations))
for permu in permus:
    mat = copy.deepcopy(matrix)
    # print("permu", permu)
    process(permu, mat)

print(ans)