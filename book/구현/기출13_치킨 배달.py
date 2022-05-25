# https://www.acmicpc.net/problem/15686
from itertools import combinations
# from collections import deque
# import copy

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            homes.append((i,j))
        elif matrix[i][j] == 2:
            chickens.append((i,j))

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def bfs(mat, a, b):

#     q = deque([(a,b,0)])
#     visit = set([(a,b)])
#     while q:
#         x, y, dist = q.popleft()

#         if mat[x][y] == 2:
#             return dist

#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]

#             if 0 <= xx < N and 0 <= yy < N and (xx, yy) not in visit:
#                 q.append((xx, yy, dist+1))
#                 visit.add((xx,yy))


def calculate_distance(home, chicken):
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

combis = list(combinations(chickens, M))
ttl_dist = int(1e9)
for combi in combis:
    combi_dist = 0
    for home in homes:
        home_chicken_dist = int(1e9)
        for chicken in combi:
            home_chicken_dist = min(home_chicken_dist, calculate_distance(home,chicken))
        combi_dist += home_chicken_dist
    ttl_dist = min(ttl_dist, combi_dist)
    # copy_mat =copy.deepcopy(matrix)
    # closed_chickens = set(chickens) - set(combi)
    # combi_dist = 0

    # for closed_chicken in closed_chickens:
    #     x,y = closed_chicken
    #     copy_mat[x][y] = 0
    # for a, b in homes:
    #     combi_dist += bfs(copy_mat, a, b)
    # ttl_dist = min(ttl_dist, combi_dist)

print(ttl_dist)