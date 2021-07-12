#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        temp=phone_book[i]
        if temp == phone_book[i+1][0:len(temp)]:
            answer=False
            return answer
    
    
    return answer