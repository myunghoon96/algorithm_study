#https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    import re
    answer = 0
    total_score = []
    p = re.compile('[0-9]{1,2}[A-Z][*#]{0,1}')
    p2 = re.compile('[1-9][0-9]')
    result = p.findall(dartResult)
    result.reverse()
    
    prevOption = ""
    for e in result:
        if p2.search(e)==None:
            score = e[0]
            bonus = e[1]
        else:
            score = e[0:2]
            bonus = e[2]
        
        if bonus == "S":
            bonus_score=1    
        elif bonus == "D":
            bonus_score=2
        elif bonus == "T":
            bonus_score=3
        calculate_score = int(score)**(bonus_score)
        
        if prevOption == "*":
            calculate_score*=2
        
        if len(e)==3:
            cur_option = e[-1]
            if cur_option == "*":
                calculate_score*=2
            elif cur_option == "#":
                calculate_score*=-1
            prevOption=cur_option
        
        else:
            prevOption=""
        
        total_score.append(calculate_score)

    answer = sum(total_score)
    return answer