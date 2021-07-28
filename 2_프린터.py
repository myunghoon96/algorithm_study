#https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities, location):
    answer = 0
    
    maxp=max(priorities)
    l = len(priorities)
    while len(priorities)>0:
        v = priorities.pop(0)
        if v == maxp:
            answer+=1          
            if location == 0:
                return answer
            maxp=max(priorities) 
            
        else:    
            priorities.append(v)
        
        if location==0:
            location = len(priorities)-1
        else:
            location-=1
  
    return answer