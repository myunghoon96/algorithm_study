# https://www.acmicpc.net/problem/1991
from collections import defaultdict, deque

#전위 순회
def preOrder(tree, node):
    print(node, end = '')
    l_child, r_child = tree[node]
    if l_child != '.':
        preOrder(tree, l_child)
    if r_child != '.':
        preOrder(tree, r_child)
    return

#중위 순회
def inOrder(tree, node):
    l_child, r_child = tree[node]
    if l_child != '.':
        inOrder(tree, l_child)
    print(node, end = '')
    if r_child != '.':
        inOrder(tree, r_child)
    return

#후위 순회
def postOrder(tree, node):
    l_child, r_child = tree[node]
    if l_child != '.':
        postOrder(tree, l_child)
    if r_child != '.':
        postOrder(tree, r_child)
    print(node, end = '')
    return

n = int(input())
tree = defaultdict(list)

for _ in range(n):
    a, b, c = input().split()
    tree[a].append(b)
    tree[a].append(c)

preOrder(tree, 'A')
print()
inOrder(tree, 'A')
print()
postOrder(tree, 'A')
print()

