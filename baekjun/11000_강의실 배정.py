#https://www.acmicpc.net/problem/11000

import sys
import heapq
n=int(sys.stdin.readline())
l=[]
cnt=0

for i in range(n):
    s,e=map(int,sys.stdin.readline().split())
    l.append((s,e))

l.sort(key=lambda x: (x[0],x[1]))
ans=0
hq=[]
heapq.heappush(hq, l[0][1])


for i in range(1,n):
    s,e=l[i]
    if s>=hq[0]:
        heapq.heappop(hq)
        heapq.heappush(hq, e)
    else:
        heapq.heappush(hq, e)

print(len(hq))