#https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        costs = defaultdict(int)      
        
        for time in times:
            source, target, cost = time
            graph[source].append((cost, target)) 
        
        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            
            while q:
                cost, target = heapq.heappop(q)
                if target not in costs:
                    costs[target]=cost
                    for c, t in graph[target]:
                        heapq.heappush(q, (c+cost, t))
            
        dijkstra(k)

        if len(costs)==n:
            return max(costs.values())
        
        return -1