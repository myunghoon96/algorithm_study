#https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node
        
        copy=Node(node.val, [])
        q=deque()
        q.append(node)
        d=dict()
        d[node]=copy
        while q:
            cur=q.popleft()

            for n in cur.neighbors:
                if n not in d:
                    q.append(n)
                    d[n]=Node(n.val, [])
                d[cur].neighbors.append(d[n])

        return copy
