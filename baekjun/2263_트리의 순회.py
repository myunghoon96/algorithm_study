# https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
in_orders = [-1] + list(map(int, sys.stdin.readline().split()))
post_orders = [-1] + list(map(int, sys.stdin.readline().split()))

positions = [-1] * (N + 1)
for i in range(1, N + 1):
    node_no = in_orders[i]
    positions[node_no] = i

#in_order: left root right
#post_order: left right root
def pre_order(in_start, in_end, p_start, p_end):
    if in_start > in_end or p_start > p_end:
        return
    
    root = post_orders[p_end]
    print(root, end= ' ')

    in_root_idx = positions[root]
    left_node_cnt = in_root_idx - in_start
    right_node_cnt = in_end - in_root_idx

    #left
    pre_order(in_start, in_root_idx - 1, p_start, p_start + left_node_cnt - 1)
    #right
    pre_order(in_root_idx + 1, in_end, p_start + left_node_cnt, p_end - 1)

pre_order(1, N, 1, N)