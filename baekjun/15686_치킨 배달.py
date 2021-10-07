#https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
# print(n,m)
homes = set()
chickens = set()
ans = 0
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == 1:
            homes.add((i,j))
        elif temp[j] == 2:
            chickens.add((i,j))

# print(homes)
# print(chickens)

def distance(home, chicken):
    return abs(home[0]-chicken[0])+abs(home[1]-chicken[1])

temp_sum_list = []
for combi_chickens in combinations(chickens, m):
    temp_sum = 0
    for home in homes:
        min_dis = 10000
        for chicken in combi_chickens:
            min_dis=min(min_dis, distance(home,chicken))
            
        # print(home, chicken, min_dis, temp_sum)
        temp_sum+=min_dis
    temp_sum_list.append(temp_sum)

# print(temp_sum_list)
print(min(temp_sum_list))
