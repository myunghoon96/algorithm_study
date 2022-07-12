# https://www.acmicpc.net/problem/2668
#cycle
import sys
sys.setrecursionlimit(int(10e6))

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    num = int(sys.stdin.readline())
    graph[num].append(i)

ans_cycle = []
def dfs(x, visit):
    global ans_cycle
    for next_node in graph[x]:
        if next_node not in visit:
            dfs(next_node, visit + [next_node])
        elif next_node in visit:
            # if len(ans_cycle) < len(visit):
            ans_cycle.extend(visit)


for i in range(1, N+1):
    dfs(i, [i])

print(len(set(ans_cycle)))
for e in sorted(list(set(ans_cycle))):
    print(e) 


# 메모리 초과
# import sys
# from itertools import combinations

# N = int(sys.stdin.readline())
# nums = [(i+1, int(sys.stdin.readline())) for i in range(N)]

# ans_line1 = []
# for length in range(1, N+1):
#     combis = list(combinations(nums, length))
#     for combi in combis:
#         line1, line2 = [], []
#         for pair in combi:
#             num1, num2 = pair
#             line1.append(num1)
#             line2.append(num2)

#         if sorted(line1) == sorted(line2):
#             if len(line1) > len(ans_line1):
#                 ans_line1 = sorted(line1)

# print(len(ans_line1))
# for e in ans_line1:
#     print(e)