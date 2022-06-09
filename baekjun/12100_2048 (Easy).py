# https://www.acmicpc.net/problem/12100

import sys
import copy

N = int(sys.stdin.readline().rstrip())
n = N
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = -1

def move_up(mat):
    global ans

    for j in range(N):
        tmp_sum = []
        for i in range(N):
            if mat[i][j] != 0:
                if len(tmp_sum) > 0 and tmp_sum[-1][1] and tmp_sum[-1][0] == mat[i][j]:
                    tmp_sum[-1][0] += mat[i][j]
                    tmp_sum[-1][1] = False
                else:
                    tmp_sum.append([mat[i][j], True])
                mat[i][j] = 0
        idx = 0
        for e in tmp_sum:
            mat[idx][j] = e[0]
            idx += 1

    return mat

def move_down(mat):
    global ans
    
    for j in range(N):
        tmp_sum = []
        for i in range(N-1, -1, -1):
            if mat[i][j] != 0:
                if len(tmp_sum) > 0 and tmp_sum[-1][1] and tmp_sum[-1][0] == mat[i][j]:
                    tmp_sum[-1][0] += mat[i][j]
                    tmp_sum[-1][1] = False
                else:
                    tmp_sum.append([mat[i][j], True])
                mat[i][j] = 0

        idx = N-1
        for e in tmp_sum:
            mat[idx][j] = e[0]
            idx -= 1
    
    return mat

def move_right(mat):
    global ans
    
    for i in range(N):
        tmp_sum = []
        for j in range(N-1, -1, -1):
            if mat[i][j] != 0:
                if len(tmp_sum) > 0 and tmp_sum[-1][1] and tmp_sum[-1][0] == mat[i][j]:
                    tmp_sum[-1][0] += mat[i][j]
                    tmp_sum[-1][1] = False
                else:
                    tmp_sum.append([mat[i][j], True])
                mat[i][j] = 0

        idx = N-1
        for e in tmp_sum:
            mat[i][idx] = e[0]
            idx -= 1

    return mat

def move_left(mat):
    global ans
    
    for i in range(N):
        tmp_sum = []
        for j in range(N):
            if mat[i][j] != 0:
                if len(tmp_sum) > 0 and tmp_sum[-1][1] and tmp_sum[-1][0] == mat[i][j]:
                    tmp_sum[-1][0] += mat[i][j]
                    tmp_sum[-1][1] = False
                else:
                    tmp_sum.append([mat[i][j], True])
                mat[i][j] = 0

        idx = 0
        for e in tmp_sum:
            mat[i][idx] = e[0]
            idx += 1

    return mat

def move(mat, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, mat[i][j])
        return

    move(move_left(copy.deepcopy(mat)), cnt+1)
    move(move_right(copy.deepcopy(mat)), cnt+1)
    move(move_up(copy.deepcopy(mat)), cnt+1)
    move(move_down(copy.deepcopy(mat)), cnt+1)

move(matrix, 0)
# matrix = move_up(matrix)
# matrix = move_down(matrix)
# matrix = move_left(matrix)
# matrix = move_right(matrix)
# matrix = move_up(matrix)

# for e in matrix:
#     print(e)

print(ans)