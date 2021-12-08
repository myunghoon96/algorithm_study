#https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        distances = [(sys.maxsize, sys.maxsize)]*n
        distances[src] = (0, 0)

        for depart,arrive,price in flights:
            graph[depart].append((price,arrive))
                      
        q = [(0, src, 0)]

        while q:
            cost, depart, stop = heapq.heappop(q)
            if depart == dst:
                return cost

            if stop <= k:
                for c, d in graph[depart]:
                    if cost+c >= distances[d][0] and stop+1 >= distances[d][1]:
                        continue
                    distances[d] = (cost+c, stop+1)
                    heapq.heappush(q, (cost+c, d, stop+1))

        return -1


