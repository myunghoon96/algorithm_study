#https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
        
    def change(num, base):
        result=""
        temp = "0123456789ABCDEF"    
        
        if num ==0:
            return "0"
        
        while num > 0 :
            num,remain = divmod(num,base)
            result+=temp[remain]
        
        return result[::-1]
        
    total = t*m
    num=0
    tempAns=""
    while len(tempAns) <= total:
        result=change(num,n)
        tempAns+=result
        num+=1

    index=0
    while True:
        if (index*m)+p-1 > total:
            break
        if (index*m)+p-1 < total:
            answer+=(tempAns[(index*m)+p-1])
        index+=1
        
    return answer