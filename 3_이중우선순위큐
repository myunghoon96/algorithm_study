#https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []
    tempList = []
    for e in operations:
        ins=e.split(' ')[0]
        num=e.split(' ')[1]
        if ins == "I":
            tempList.append(int(num))
            tempList.sort()
        elif ins == "D":
            try:
                if num == "-1":
                    del tempList[0]

                if num == "1":
                    del tempList[-1] 
            except:
                continue
                
    # print(tempList)
    
    try:
        answer.append(int(tempList[-1]))
        answer.append(int(tempList[0]))
    except:
        answer=[0,0]
    return answer