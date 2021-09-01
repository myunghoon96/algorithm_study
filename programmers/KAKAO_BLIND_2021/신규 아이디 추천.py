#https://programmers.co.kr/learn/courses/30/lessons/72410

import re
def solution(new_id):
    answer = ''
    
    new_id=new_id.lower()
    
    for e in new_id:
        if e.isalnum() or e in "-_.":
            answer+=e
    
    answer = re.sub("[.]{2,}", ".", answer)

    if len(answer)>0 and answer[0]==".":
        answer=answer[1:]
    if len(answer)>0 and answer[-1]==".":
        answer=answer[:-1]
    
    if len(answer)==0:
        answer="a"
        
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]==".":
            answer=answer[:-1]
            
    if len(answer)<=2:
        time = 3-len(answer)
        answer = answer + answer[-1]*time
    
    return answer