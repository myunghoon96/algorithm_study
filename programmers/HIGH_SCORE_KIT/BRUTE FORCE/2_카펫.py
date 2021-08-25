#

def solution(brown, yellow):
    answer = []    
    area=brown+yellow   
    l=[]
    
    for i in range(1, (area+1)//2):
        if area%i==0:
            l.append((i, area//i))       
    
    for r,c in l:
        if yellow==(r-2)*(c-2):
            answer = [r,c]
            break
    
    answer.sort(reverse=True)
    return answer