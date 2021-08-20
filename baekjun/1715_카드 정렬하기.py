#https://www.acmicpc.net/problem/1715

import heapq

hq=[]

n=int(input())
ans=0
for i in range(n):
    heapq.heappush(hq,int(input()))

while len(hq)>=2:

    a=heapq.heappop(hq)
    b=heapq.heappop(hq)
    ans+=a+b
    heapq.heappush(hq,a+b)

print(ans)