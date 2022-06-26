# https://www.acmicpc.net/problem/16235

import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
age = [[[]*N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    age[x-1][y-1].append(z)

nutritions = [[5]*N for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    #spring
    dead_trees = []
    for i in range(N):
        for j in range(N):
            if len(age[i][j]) > 0:
                #deque appendleft
                age[i][j].sort()
                new_age = []
                for k in range(len(age[i][j])):
                    if nutritions[i][j] >= age[i][j][k]:
                        nutritions[i][j] -= age[i][j][k]
                        age[i][j][k] += 1
                        new_age.append(age[i][j][k])
                    else:
                        dead_trees.append((i,j,age[i][j][k]))
                age[i][j] = new_age

    #summer
    for dead_tree in dead_trees:
        x, y, tree_age = dead_tree
        nutritions[x][y] += int(tree_age//2)

    #autumn
    for x in range(N):
        for y in range(N):

            if len(age[x][y]) > 0:
                for tree_age in age[x][y]:
                    if tree_age % 5 == 0:
                        for idx in range(8):
                            xx = x + dx[idx]
                            yy = y + dy[idx]
                            if 0 <= xx < N and 0 <= yy < N:
                                #deque appendleft
                                age[xx][yy].append(1)

    #winter
    for i in range(N):
        for j in range(N):
            nutritions[i][j] += A[i][j]

tree_cnt = 0
for i in range(N):
    for j in range(N):
        if len(age[i][j]) > 0:
            tree_cnt += len(age[i][j])
print(tree_cnt)