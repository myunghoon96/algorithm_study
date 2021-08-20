#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 0
    
    d=dict()
    
    for e,c in clothes:
        if d.get(c)==None:
            d[c]=1
        else:
            d[c]+=1
            
    # print("keys ",len(d.keys()))
    # print("values ",d.values())
    
    if len(d.keys())==1:
        answer=list(d.values())[0]
        
    else:
        temp=1
        for k,v in d.items():
            temp*=(v+1)
            
        answer=temp-1
    
    return answer