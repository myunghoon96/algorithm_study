#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def checkPrime(num):
    if num<2:
        return False #Not Prime Num
    for i in range(2,num):
        if(num%i==0):
            return False #Not Prime Num
    return True #Yes Prime Num

def solution(numbers):
    answer = 0
    numList =[]
    totalNum = 0
    ansList=set()
    
    for e in numbers:
        numList.append(e)
    
    totalNum=len(numList)
    while(totalNum>0):
        for i in permutations(numList, totalNum):
            tempStr=""
            for index, s in enumerate(i):
                tempStr+=s
            ansList.add(int(tempStr))
        totalNum-=1

    for e in ansList:
        if checkPrime(e) == True:
            answer+=1
    
    return answer