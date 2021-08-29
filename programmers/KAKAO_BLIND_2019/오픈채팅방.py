#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    d=dict()
    
    for r in record:
        op=r.split(" ")[0]
        if op=="Enter":
            uid=r.split(" ")[1]
            nickname=r.split(" ")[2]
            d[uid]=nickname
            answer.append(uid+"님이 들어왔습니다.")
        
        elif op=="Leave":
            uid=r.split(" ")[1]
            answer.append(uid+"님이 나갔습니다.")
        
        elif op=="Change":
            uid=r.split(" ")[1]
            nickname=r.split(" ")[2]
            d[uid]=nickname
    
    for i,a in enumerate(answer):
        uid=a.split(" ")[0][:-2]
        answer[i]=answer[i].replace(uid, d[uid])
    
        
    return answer