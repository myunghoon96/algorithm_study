#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i,p in enumerate(completion):  
        if(p!=participant[i]):
            answer=participant[i]
            return answer
    answer=participant[-1]
    return answer