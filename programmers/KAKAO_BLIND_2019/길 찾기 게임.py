#https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**6)

class tree:
    def __init__(self, idx, x, y):
        self.idx=idx
        self.x=x
        self.y=y
        self.left= None
        self.right= None

preList = []
def preorder(node):
    global preList
    if node == None:
        return
    
    preList.append(node.idx+1)
    # print(node.idx, (node.x, node.y))
    preorder(node.left)
    preorder(node.right)

    
postList = []
def postorder(node):
    global postList
    if node == None:
        return
  
    postorder(node.left)
    postorder(node.right)
    # print(node.idx, (node.x, node.y))
    postList.append(node.idx+1)


    
def solution(nodeinfo):
    answer = []
    index = [i for i in range(len(nodeinfo))]

    nodes = list(zip(index,nodeinfo))
    nodes.sort(key=lambda x:(x[1][1],-x[1][0]), reverse=True)
    # print(nodes)    
    
    root = None
    for i, e in enumerate(nodes):
        idx, x, y = e[0], e[1][0], e[1][1]
        if i == 0 :
            root = tree(idx,x,y)
        else:
            cur = root
            while True:
                if cur.x > x:
                    if cur.left == None:
                        cur.left = tree(idx,x,y)
                        break
                    else:
                        cur = cur.left
                        
                elif cur.x < x:
                    if cur.right == None:
                        cur.right = tree(idx,x,y)
                        break
                    else:
                        cur = cur.right
    
    preorder(root)
    postorder(root)
    
    answer.append(preList)
    answer.append(postList)

    return answer