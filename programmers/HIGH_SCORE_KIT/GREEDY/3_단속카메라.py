#https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    
    if len(routes)==0:
        return 0
    
    camera = routes[0][1]
    answer = 1
    for start,end in routes[1:]:
        if start>camera:
            answer+=1
            camera=end

    return answer