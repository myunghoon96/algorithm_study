#https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    cache=deque()
    
    if cacheSize==0:
        answer=len(cities)*5
        return answer
    
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
        
    for e in cities:
        if e in cache:
            cache.remove(e)
            cache.append(e)
            answer+=1
        else:
            if len(cache)==cacheSize:
                cache.popleft()
            cache.append(e)
            answer+=5
    
    return answer