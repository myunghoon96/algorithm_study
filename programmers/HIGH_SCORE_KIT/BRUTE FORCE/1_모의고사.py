#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    s1=0
    s2=0
    s3=0
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    
    for i,e in enumerate(answers):
        
        if e==p1[i%5]:
            s1+=1
        if e==p2[i%8]:
            s2+=1
        if e==p3[i%10]:
            s3+=1
             

    maxVal=max(s1,(max(s2,s3)))

    if s1==maxVal:
        answer.append(1)
    if s2==maxVal:
        answer.append(2)
    if s3==maxVal:
        answer.append(3)
    return answer