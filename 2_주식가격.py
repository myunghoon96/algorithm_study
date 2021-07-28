#https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(0,len(prices)):
        count=0
        for k in range(i,len(prices)):
            if(prices[i]<=prices[k]):
                count+=1
                if(k==len(prices)-1):
                    answer.append(count-1)
            else:
                answer.append(count)
                break
    return answer