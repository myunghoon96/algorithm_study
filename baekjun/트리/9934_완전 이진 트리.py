#https://www.acmicpc.net/problem/9934

k = int(input())
buildings = list(map(int, input().split()))

answer = [[] for _ in range(k)]
depth = 0

def process(buildings, depth):
    # print(buildings, depth)
    mid = len(buildings)//2

    left_tree , right_tree = buildings[:mid], buildings[mid+1:]
    answer[depth] += [buildings[mid]]

    if len(left_tree) == 1 and len(right_tree) == 1:
        answer[k-1] += [left_tree[0]]
        answer[k-1] += [right_tree[0]]
        return

    process(left_tree, depth+1)
    process(right_tree, depth+1)
    return

process(buildings, 0)
for e in answer:
    print(*e)
