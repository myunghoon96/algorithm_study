#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        from collections import deque
        
        row, col = len(grid), len(grid[0])

        visit = [[0 for _ in range(col)] for _ in range(row)]
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        def bfs(i,j):
            q = deque()    
            q.append((i,j))
            
            visit[i][j]=1
            
            while q:
                x,y = q.popleft()
                
                for index in range(4):
                    xx = x+dx[index]
                    yy = y+dy[index]
                    
                    if 0<=xx<row and 0<=yy<col and visit[xx][yy]==0 and grid[xx][yy]=="1":
                        q.append((xx,yy))
                        visit[xx][yy]=1
        
        
        cnt=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and visit[i][j]==0:
                    bfs(i,j)
                    cnt+=1
        
        return cnt