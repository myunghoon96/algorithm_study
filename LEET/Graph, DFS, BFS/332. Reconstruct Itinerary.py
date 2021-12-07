#https://leetcode.com/problems/reconstruct-itinerary/


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        tickets.sort()
        for ticket in tickets:
            depart, arrive = ticket
            graph[depart].append(arrive)

        print(graph)
        
        path = []
        def dfs(depart):            
                    
            while graph[depart]:
                arrive = graph[depart].pop(0)
                dfs(arrive)

            path.append(depart)  
        dfs("JFK")
            
        return path[::-1]