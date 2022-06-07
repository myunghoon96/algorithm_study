# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
        
    list_1d = []

    for i in range(left, right+1):
        list_1d.append(max(1+ i//n, 1+ i%n))
    
    
    return list_1d
