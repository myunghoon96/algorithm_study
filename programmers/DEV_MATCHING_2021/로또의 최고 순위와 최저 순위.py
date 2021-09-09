#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    zeros = lottos.count(0)
    correct = 0
    d = {2:5, 3:4, 4:3, 5:2, 6:1}
    
    for num in lottos:
        if num == 0:
            continue
        #not zero        
        if num in win_nums:
            correct += 1
    
    best = correct+zeros
    worst = correct
    
    if d.get(best) != None:
        answer.append(d[best])
    else:
        answer.append(6)
    
    if d.get(worst) != None:
        answer.append(d[worst])
    else:
        answer.append(6)
    
    return answer