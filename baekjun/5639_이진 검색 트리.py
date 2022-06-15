# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)

pre_orders = []
while True:
    try: 
        num = int(sys.stdin.readline().rstrip())
        pre_orders.append(num)
    except:
        break

def post_order(start, end):
    if start >= end:
        return

    root = pre_orders[start]

    mid = end
    for i in range(start, end):
        if pre_orders[i] > root:
            mid = i
            break
    
    #left tree
    post_order(start+1, mid)
    #right tree
    post_order(mid, end)
    #root
    print(root)
    return

post_order(0, len(pre_orders))