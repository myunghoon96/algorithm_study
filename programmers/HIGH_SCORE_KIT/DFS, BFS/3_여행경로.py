#https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []
    d = dict()
    stack = []
    
    for a,b in tickets:
        if d.get(a)==None:
            d[a]=[b]
        else:
            d[a].append(b)

    for a in d.keys():
        d[a].sort(reverse=True)

    stack.append("ICN")
    while stack:
        temp = stack[-1]
        
        if temp not in d.keys() or len(d[temp]) == 0:
            answer.append(stack.pop())
        
        else: 
            stack.append(d[temp].pop())

    answer.reverse()
        
    return answer