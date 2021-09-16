#https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import deque
def solution(gems):
    answer = []
    ansList = []
    kind = len(set(gems))
    d = dict()

    start=0
    end = 0
    while start<len(gems) and end<len(gems):
        if d.get(gems[end]) != None:
            d[gems[end]]+=1
        else:
            d[gems[end]]=1
        end+=1
        # print(d, len(d), kind)
        if kind == len(d):
            # print(d)
            while start<end:
                d[gems[start]]-=1
                if d[gems[start]]==0:
                    del d[gems[start]]                   
                start+=1
                
                if kind != len(d):
                    ansList.append((start, end, end-start))
                    break
                
    # print(ansList)
    ansList.sort(key = lambda x:(x[2], x[0], x[1]))
    answer.append(ansList[0][0])
    answer.append(ansList[0][1])
    return answer