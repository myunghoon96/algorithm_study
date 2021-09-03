#https://programmers.co.kr/learn/courses/30/lessons/72413

import heapq

def solution(n, s, a, b, fares):
    answer = float("inf")
    
    g = [[] for _ in range(n+1)]
    
    for start,end,cost in fares:
        g[start].append([cost,end])
        g[end].append([cost,start])

    def dijkstra(start, end):
        
        costList=[float("inf") for _ in range(n+1)]
        costList[start]=0
        
        q=[]
        q.append([0,start])
        heapq.heapify(q)
        
        while q:
            cur_cost,cur_position = heapq.heappop(q)

            if cur_cost>costList[cur_position]:
                continue

            for e in g[cur_position]:
                
                next_cost, next_position = e[0], e[1]
                
                if next_cost+cur_cost < costList[next_position]:

                    heapq.heappush(q, [next_cost+cur_cost,next_position])
                    costList[next_position]=next_cost+cur_cost

        return costList[end]

    for separate in range(1,n+1):
        answer = min(answer, dijkstra(s,separate)+dijkstra(separate,a)+dijkstra(separate,b))

    return answer