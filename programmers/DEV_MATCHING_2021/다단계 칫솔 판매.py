#https://programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    answer = []
    parent = dict()
    money = dict()
    for i, e in enumerate(enroll):
        parent[e] = referral[i]
        money[e] = 0
   
    for i, child in enumerate(seller):
        money100 = amount[i] * 100
        money[child] += money100

        while True:
            fee = money100//10
            if fee<1:
                break
            
            money[child]-=fee
            
            pr = parent[child]
            if pr == '-':
                break
                
            money[pr]+=fee
            child = pr
            money100 = fee
            
    for value in money.values():
        answer.append(value)
    
    return answer
