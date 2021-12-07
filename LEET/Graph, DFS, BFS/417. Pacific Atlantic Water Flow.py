class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

        row,col=len(heights), len(heights[0])

        
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
       
        def bfs(q):
            visit = [[0 for _ in range(col)] for _ in range(row)]
            ans = set()
            while q:
                x,y = q.popleft()
                visit[x][y]=1
                ans.add((x,y))
                for i in range(4):
                    xx=x+dx[i]
                    yy=y+dy[i]
                    
                    if 0<=xx<row and 0<=yy<col and visit[xx][yy]==0 and heights[xx][yy]>=heights[x][y]:
                        q.append((xx,yy))
                        
                        
            return ans 
        
        pq=deque()
        for i in range(row):
            pq.append((i,0))
        for j in range(1, col):
            pq.append((0,j))      
        
        aq=deque()
        for i in range(row):
            aq.append((i,col-1))
        for j in range(col):
            aq.append((row-1,j))
    
        p_visit = bfs(pq)
        a_visit =bfs(aq)

        return (p_visit & a_visit)