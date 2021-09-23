#https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

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