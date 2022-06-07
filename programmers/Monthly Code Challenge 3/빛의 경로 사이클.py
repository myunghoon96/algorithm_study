# https://programmers.co.kr/learn/courses/30/lessons/86052

from collections import deque

def solution(grid):
    answer = []
    direcs = [0, 1, 2, 3] # north, east, south west
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    
    def bfs(x, y , d):
        q = deque([(x, y, d, 0)])
        visit.add((x, y, d, 0))
        max_dist = -1
        while q:
            x, y, direc, dist = q.popleft()
            max_dist = max(max_dist, dist)
            
            xx = (x + moves[direc][0])%rows
            yy = (y + moves[direc][1])%cols
            grid_direc = grid[xx][yy]
            if grid_direc == 'S':
                new_direc = direc
            elif grid_direc == 'L':
                new_direc = (direc - 1) % 4
            elif grid_direc == 'R':
                new_direc = (direc + 1) % 4
            
            if (xx, yy, new_direc) not in visit:
                visit.add((xx, yy, new_direc))
                q.append((xx, yy, new_direc, dist+1))
        # print(max_dist)
        return max_dist
        
    for d in range(4):
        for x in range(rows):
            for y in range(cols):
                if (x,y,d) not in visit:
                    answer.append(bfs(x,y,d))
                    # print(x,y,d)
    answer.sort()
    return answer