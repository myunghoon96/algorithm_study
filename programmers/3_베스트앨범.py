#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    d=dict()
    for i,e in enumerate(genres):

        if d.get(e)==None:
            d[e]=plays[i]
        else:
            d[e]+=plays[i]
            
    d=list(d.items())
    d.sort(key=lambda x:(x[1],x[0]), reverse=True)
    
    for e in d:
        g=e[0]
        temp=[]
        for i,e in enumerate(genres):
            if g==e:
                temp.append((i,plays[i]))  

        temp.sort(key=lambda x:(x[1],x[0]), reverse=True)

        if len(temp)>=2:
            if temp[0][1]==temp[1][1] and temp[0][0]>temp[1][0]:
                answer.append(temp[1][0])
                answer.append(temp[0][0])
            else:
                answer.append(temp[0][0])
                answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
    return answer