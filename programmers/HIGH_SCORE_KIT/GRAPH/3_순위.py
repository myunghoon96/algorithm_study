#https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    
    win = dict()
    lose = dict()
    
    for i in range(n+1):
        win[i]=set()
        lose[i]=set()
    
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
        
    for i in range(1,n+1):
        for loser in win[i]:
            lose[loser].update(lose[i])
        for winner in lose[i]:
            win[winner].update(win[i])    
                
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
    
    return answer