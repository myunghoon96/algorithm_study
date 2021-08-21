#https://programmers.co.kr/learn/courses/30/lessons/42860#

def solution(name):
    answer = 0
    cur = 0

    l=[0 for _ in range(len(name))]
    
    for i,e in enumerate(name):
        if e!="A":
            v = min(ord(e)-ord('A'),ord('Z')-ord(e)+1)
            l[i]=v
        
    while True:
        answer+=l[cur]
        l[cur]=0
        
        if sum(l)==0:
            return answer
        
        leftMove=1
        while l[cur-leftMove]==0:     
            leftMove+=1
        
        rightMove=1
        while l[cur+rightMove]==0:            
            rightMove+=1
        
        minMove=min(rightMove,leftMove)
        answer+=minMove
        if minMove==rightMove:
            cur+=rightMove
        else:
            cur-=leftMove
