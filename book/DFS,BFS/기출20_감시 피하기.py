# https://www.acmicpc.net/problem/18428
from itertools import combinations
import copy 
N = int(input())
matrix = [list(input().split()) for _ in range(N)]

empty_set = set()
teacher_set = set()
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'X':
            empty_set.add((i,j))
        elif matrix[i][j] == 'T':
            teacher_set.add((i,j))

def is_student_safe(mat):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for x, y in teacher_set:
        for i in range(4):
            move = 1
            while True:
                xx = x + dx[i] * move
                yy = y + dy[i] * move
                if 0 <= xx < N and 0 <= yy < N and mat[xx][yy] != 'O':
                    if mat[xx][yy] == 'X':
                        mat[xx][yy] = 'T'
                    elif mat[xx][yy] == 'S':
                        return False
                    move += 1                
                else:
                    break

    return True

ans = "NO"
for combis in list(combinations(empty_set, 3)):
    tmp_mat = copy.deepcopy(matrix)
    for x,y in combis:
        tmp_mat[x][y] = 'O'
        if is_student_safe(tmp_mat):
            ans = "YES"

print(ans)