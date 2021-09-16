#https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def bfs(x,y, direc, boardSize,board):
    ansList = []
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    q = deque()   
    q.append((x,y,0,direc))

    money=[[float('inf')]*boardSize for _ in range(boardSize)]
    money[0][0]=0
    while q:
        x,y,cost, pre_direction = q.popleft()
        if x==boardSize-1 and y==boardSize-1:
            ansList.append(cost)

        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]

            cur_direction = i
            
            new_cost = 100+cost if pre_direction==cur_direction else 600+cost
            if 0<=xx<boardSize and 0<=yy<boardSize and board[xx][yy]==0 and money[xx][yy]>new_cost:

                money[xx][yy]=new_cost
                q.append((xx,yy,new_cost, cur_direction))
    
    return ansList
        
def solution(board):
    answer = 0
    boardSize = len(board)

    ansList = bfs(0,0,0,boardSize, board)
    ansList2 = bfs(0,0,2,boardSize, board)
    
    answer = min(min(ansList),min(ansList2))

    return answer