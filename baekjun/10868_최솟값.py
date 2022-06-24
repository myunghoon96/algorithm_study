# https://www.acmicpc.net/problem/10868
# segment tree, 세그먼트 트리
import sys, math
sys.setrecursionlimit(10**6)

def init_segment_tree(node, node_start, node_end):
    if node_start == node_end:
        tree[node] = nums[node_start]
        return tree[node]

    mid = (node_start + node_end) //2
    tree[node] = min(init_segment_tree(node*2, node_start, mid), init_segment_tree(node*2 + 1, mid+1, node_end))
    return tree[node]

#node_start node_end tree 범위, left right query 범위
def query_segment_tree(node, node_start, node_end, left, right):
    if node_end < left or node_start > right:
        return 1000000001

    elif left <= node_start and right >= node_end:
        return tree[node]
    

    mid = (node_start + node_end) //2
    return min(query_segment_tree(node*2, node_start, mid, left, right), query_segment_tree(node*2+1, mid + 1, node_end, left, right))

N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

h = int(math.ceil(math.log2(N)))
# tree_size = 1 << (h + 1)
tree_size = 2 ** (h + 1)
tree = [0] * (tree_size)

init_segment_tree(1, 0, N-1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(query_segment_tree(1, 0, N-1, a-1, b-1))
