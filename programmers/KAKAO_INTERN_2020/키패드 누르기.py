#https://programmers.co.kr/learn/courses/30/lessons/67256

from collections import deque

def distance(target, cur):
    matrix = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    cur_x, cur_y = 0, 0
    for i in range(4):
        for j in range(3):
            if matrix[i][j]==cur:
                # print("cur ", (i,j))
                cur_x, cur_y = i, j
    
    visit=set()
    visit.add((cur_x, cur_y))
    q=deque()
    q.append((cur_x, cur_y, 0))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    dis = 0
    
    while(q):
        x,y, dis=q.popleft()
        if matrix[x][y]==target:
            # print("FINISH DIS ", dis)
            return dis 
        
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            
            if 0<=xx<4 and 0<=yy<3 and (xx,yy) not in visit:
                visit.add((xx,yy))
                q.append((xx,yy, dis+1))


def solution(numbers, hand):
    answer = ''
    l_hand='*'
    r_hand='#'
    for number in numbers:
        number = str(number)
        if number in ['1','4','7']:
            answer+='L'
            l_hand = number
        elif number in ['3','6','9']:
            answer+='R'
            r_hand = number

        else:
            if distance(number, l_hand) < distance(number, r_hand):
                answer+='L'
                l_hand = number
            elif distance(number, l_hand) > distance(number, r_hand):
                answer+='R'
                r_hand = number
            else:
                if hand=='left':
                    answer+='L'
                    l_hand=number
                else:
                    answer+='R'
                    r_hand=number

    return answer