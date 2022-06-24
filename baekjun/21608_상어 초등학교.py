# https://www.acmicpc.net/problem/21608

import sys

N = int(sys.stdin.readline())
likes = [[] for _ in range((N**2)+1)]
matrix = [[0]*N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def most_like_neighbors(like_list):
    empty_list = []
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 0:
                empty_list.append((x, y))
    
    like_cnt = -1
    cur_candidates = []
    for x,y in empty_list:
        tmp_cnt = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] in like_list:
                tmp_cnt += 1       
        if tmp_cnt > like_cnt:
            like_cnt = tmp_cnt
            cur_candidates = [(x, y)]
        elif tmp_cnt == like_cnt:
            cur_candidates.append((x, y))
    return cur_candidates

def most_empty_neighbors(cur_candidates):
    empty_cnt = -1
    empty_xy = (-1, -1)

    for x,y in cur_candidates:
        tmp_cnt = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] == 0:
                tmp_cnt += 1

        if tmp_cnt > empty_cnt:
            empty_cnt = tmp_cnt
            empty_xy = (x, y)

    return empty_xy

def calculate():
    score = 0
    for x in range(N):
        for y in range(N):
            tmp_cnt = 0
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] in likes[matrix[x][y]]:
                    tmp_cnt += 1
            if tmp_cnt !=0:
                score += 10**(tmp_cnt-1)
    return score

for _ in range(N**2):
    tmp_input = list(map(int, sys.stdin.readline().split()))
    student, like_students = tmp_input[0], tmp_input[1:]
    likes[student] = like_students
    # print("student, like_students", student, like_students)
    #1
    candidates = most_like_neighbors(like_students)
    # print("candidates", candidates)ㅌㅈ
    #2, 3
    (x, y) = most_empty_neighbors(candidates)

    matrix[x][y] = student
   
score = calculate()
print(score)