#https://programmers.co.kr/learn/courses/30/lessons/42746#

def solution(numbers):
    answer = ''

    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])*3
        
    numbers.sort(key = lambda x:x, reverse=True)

    for e in numbers:
        answer+=e[:len(e)//3]
    
    if answer[0]=="0":
        answer="0"
    
    return answer