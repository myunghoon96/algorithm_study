#https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def bfs(n,board):
    
    q=deque()
    q.append((0,0,0,1,0))
    visit=set()
    visit.add(((0,0),(0,1)))

    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        
        if x1==n-1 and y1==n-1:
            # print(x1,y1,x2,y2,cnt)
            return cnt
        
        if x2==n-1 and y2==n-1:
            # print(x1,y1,x2,y2,cnt)
            return cnt
        
        #right two empty
        if y1+1<n and y2+1<n and board[x1][y1+1]==0 and board[x2][y2+1]==0:
            #move
            pair = [(x1,y1+1),(x2,y2+1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x1,y1+1,x2,y2+1,cnt+1))
                visit.add(pair)
            
            pair = [(x1,y1),(x1,y1+1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x1,y1,x1,y1+1,cnt+1))
                visit.add(pair)

            pair = [(x2,y2),(x2,y2+1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x2,y2,x2,y2+1,cnt+1))
                visit.add(pair)
            
            
        #left two empty
        if y1-1>=0 and y2-1>=0 and board[x1][y1-1]==0 and board[x2][y2-1]==0:
            #move
            pair = [(x1,y1-1),(x2,y2-1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x1,y1-1,x2,y2-1,cnt+1))
                visit.add(pair)
                
            pair = [(x1,y1),(x1,y1-1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x1,y1,x1,y1-1,cnt+1))
                visit.add(pair)

            pair = [(x2,y2),(x2,y2-1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit:
                q.append((x2,y2,x2,y2-1,cnt+1))
                visit.add(pair)
            
        #down two empty
        if x1+1<n and x2+1<n and board[x1+1][y1]==0 and board[x2+1][y2]==0:
            #move
            pair = [(x1+1,y1),(x2+1,y2)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x1+1,y1,x2+1,y2,cnt+1))
                visit.add(pair)
            #rotate1 
            pair = [(x1,y1),(x1+1,y1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x1,y1,x1+1,y1,cnt+1))
                visit.add(pair)
            #rotate2    
            pair = [(x2,y2),(x2+1,y2)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x2,y2,x2+1,y2,cnt+1))
                visit.add(pair)
                
        #up two emty
        if x1-1>=0 and x2-1>=0 and board[x1-1][y1]==0 and board[x2-1][y2]==0:
            #move
            pair = [(x1-1,y1),(x2-1,y2)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x1-1,y1,x2-1,y2,cnt+1))
                visit.add(pair)  
            #rotate1    
            pair = [(x1,y1),(x1-1,y1)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x1,y1,x1-1,y1,cnt+1))
                visit.add(pair)      
            #rotate2    
            pair = [(x2,y2),(x2-1,y2)]
            pair.sort(key=lambda x:(x[0],x[1]))
            pair=tuple(pair)
            if pair not in visit: 
                q.append((x2,y2,x2-1,y2,cnt+1))
                visit.add(pair)      


    # temp=list(visit)
    # temp.sort(key=lambda x:(x[0],x[1]))
    # print(temp) 

def solution(board):
    answer = 0
    
    answer = bfs(len(board),board)
    
    return answer