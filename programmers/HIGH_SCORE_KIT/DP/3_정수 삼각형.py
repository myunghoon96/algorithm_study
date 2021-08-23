#https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0
    
    for i,l in enumerate(triangle):
        if i==0:
            continue
        for j, e in enumerate(l):
            if j==0:
                l[j]+=triangle[i-1][0]
            elif j==len(l)-1:
                l[j]+=triangle[i-1][-1]
            else:
                l[j]+=max(triangle[i-1][j-1], triangle[i-1][j])
                
    answer=max(triangle[-1])
    return answer