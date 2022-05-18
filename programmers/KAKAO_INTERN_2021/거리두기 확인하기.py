#https://programmers.co.kr/learn/courses/30/lessons/81302#fn1


from collections import deque

def solution(places):
    answer = []
    
    def bfs(matrix):
        start_list = []
        rows = len(matrix)
        cols = len(matrix[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'P':
                    start_list.append((i,j,0))
        
        for start in start_list:
            q = deque()
            visit = set()
            start_x,start_y,dist = start[0], start[1], start[2]
            q.append((start_x,start_y,dist))
            visit.add((start_x,start_y))

            while q:
                x,y,dist = q.popleft()
                
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    
                    if 0<=xx<rows and 0<=yy<cols and (xx,yy) not in visit and matrix[xx][yy] != 'X':
                        visit.add((xx,yy))
                        q.append((xx,yy,dist+1))
                        if matrix[xx][yy] == 'P':
                            if dist+1 <= 2:
                                return 0
        return 1
            
        
    
    for matrix in places:
        result = bfs(matrix)
        answer.append(result)
    return answer



#################################


from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(input_x,input_y,matrix):
    q=deque()    
    q.append((input_x,input_y,0))
    visit=set()
    visit.add((input_x,input_y))
    result = []
    
    while q:
        x,y,dist = q.popleft()
        
        if dist >1:
            break
        
        if matrix[x][y]=='P':
            result.append((x,y,dist))
        
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            
            if 0<=xx<5 and 0<=yy<5 and matrix[xx][yy]!='X' and (xx,yy) not in visit:
                q.append((xx,yy,dist+1))
                visit.add((xx,yy))   
                
    if len(result) > 1:
        return False
    else:
        return True
def solution(places):
    answer = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    if bfs(i,j,place) == False:
                        flag=False
        if flag == True:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer