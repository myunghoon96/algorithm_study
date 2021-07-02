#https://www.acmicpc.net/problem/1753
import heapq
import sys
inf= sys.maxsize

vNum,eNum = map(int, sys.stdin.readline().split())
start=int(sys.stdin.readline())

graph=[[] for _ in range(vNum+1)]
distanceList=[inf for _ in range(vNum+1)]

for i in range(eNum):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0, start))
    distanceList[start]=0
    while q:
        sum, node=heapq.heappop(q)
        if sum>distanceList[node]:
            continue
        
        for n,w in graph[node]:
            if w+sum<distanceList[n]:
                distanceList[n]=w+sum
                heapq.heappush(q,(w+sum, n))
 

dijkstra(start)
for i in range(1,vNum+1):
    if distanceList[i]==inf:
        print("INF")
    else:
        print(distanceList[i])