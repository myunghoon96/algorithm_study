
#https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    answer = 0
    reverse = list(zip(*relation))    
    ansList = []
    index = [i for i in range(len(relation[0]))]
 
    for size in range(1, len(relation[0])+1):
        for combiIndex in combinations(index, size):
            combi = []

            for idx in combiIndex:
                combi.append(reverse[idx])
            combi = list(combi)
            combiZip = list(zip(*combi))
            # print(combi, combiZip)
            if len(combiZip) == len(set(combiZip)):
                # print("unique")
                
                addFlag=True
                for e in ansList:
                    if set(e).issubset(combiIndex):
                        # print("subset")
                        addFlag = False
                        break
    
                if addFlag:
                    ansList.append(combiIndex)
                
    # for e in ansList:    
    #     print(e)
    return len(ansList)