#https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]

    for i in range(1,9):
        numSet = set()
        numSet.add(int(str(N)*i))
        for j in range(1,i):
            for x in dp[j]:
                for y in dp[i-j]:
                    numSet.add(x+y)
                    numSet.add(x-y)
                    numSet.add(x*y)
                    if y !=0:
                        numSet.add(x//y)
        
        if number in numSet:
            return i
        
        dp[i]=numSet
    return -1
    
    return answer