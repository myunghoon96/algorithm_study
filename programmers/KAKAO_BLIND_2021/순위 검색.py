#https://programmers.co.kr/learn/courses/30/lessons/72412

import bisect
from itertools import combinations
def solution(info, query):
    answer = []
    d = dict()
    
    for information in info:
        temp = information.split(" ")
        score = int(temp[-1])
        
        for eNum in range(0,5):
            indexs = combinations([0,1,2,3], eNum)
            for index in indexs:
                tempKey = ""
                for i in range(0,4):
                    if i in index:
                        tempKey+=temp[i]
                    else:
                        tempKey+="-"
                
                if d.get(tempKey) != None:
                    d[tempKey].append(score)
                else:
                    d[tempKey]=[score]
         
    for key in d.keys():
        d[key].sort()
 
    for q in query:
        q = q.replace(" and", "").split(" ")
        score = int(q[-1])
        q="".join(q[:-1])
        # print("query ",q)
        ans=0
        if d.get(q) != None:
            ans = len(d[q]) - bisect.bisect_left(d[q], score)
                
        answer.append(ans)

    return answer


# def solution(info, query):
#     answer = []
#     people = []
    
#     for e in info:
#         a,b,c,d,e = e.split(" ")
#         people.append((a,b,c,d,e))
#     # for p in people:
#     #     print(p)
#     for q in query:
#         a,b,c,d,e = q.replace(" and", "").split(" ")
#         # print("query ",a,b,c,d,e)
#         ans=0
#         for p in people:
#             if int(p[4])<int(e):
#                 continue
#             if a!="-" and a!=p[0]:
#                 continue
#             if b!="-" and b!=p[1]:
#                 continue
#             if c!="-" and c!=p[2]:
#                 continue
#             if d!="-" and d!=p[3]:
#                 continue
#             # print(p)
#             ans+=1   
#         answer.append(ans)
#     return answer