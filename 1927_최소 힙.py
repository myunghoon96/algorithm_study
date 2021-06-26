#https://www.acmicpc.net/problem/1927

import heapq as hq
import sys
heap=[]
n=int(sys.stdin.readline())

for i in range(n):
    temp=int(sys.stdin.readline())

    if temp==0:
        if len(heap)==0:
            print(0)
        else:
            print(hq.heappop(heap))

    else:
        hq.heappush(heap, temp)