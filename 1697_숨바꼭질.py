#https://www.acmicpc.net/source/24902358

import sys
from collections import deque
n, k=map(int,(sys.stdin.readline().split()))


def bfs():

    queue = deque()
    queue.append([0, n])
    visit=[0 for _ in range(100001)]

    while queue:

        temp=queue.popleft()
        node=temp[1]
        ans=temp[0]

        if node==k:
            return ans

        if node<=(100000-1) and visit[node+1]==0:
            queue.append([ans+1, node+1])
            visit[node+1]=1
        if node-1>=0 and visit[node-1]==0:
            queue.append([ans+1, node-1])
            visit[node - 1] = 1
        if node<=(100000/2) and visit[node*2]==0:
            queue.append([ans+1, node*2])
            visit[node * 2] = 1

print(bfs())