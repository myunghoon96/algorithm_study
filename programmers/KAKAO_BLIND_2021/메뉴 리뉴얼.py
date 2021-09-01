#https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    d = dict()

    for order in orders:
        order = sorted(list(order))
        for courseNum in course:
            l = list(combinations(order, courseNum))
            for e in l:
                if d.get(''.join(e))!=None:
                    d[''.join(e)]+=1
                else:
                    d[''.join(e)]=1
    
    for courseNum in course:
        maxOrder = -1
        
        for k,v in d.items():
            if len(k) == courseNum:
                if v>maxOrder:
                    maxOrder=v
        
        if maxOrder < 2:
            continue
        
        for k,v in d.items():
            if len(k) == courseNum:
                if v==maxOrder:
                    answer.append(k)
        
    answer.sort()
    return answer