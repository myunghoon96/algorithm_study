#https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
def solution(progresses, speeds):
    answer = []
    remain=deque()
    
    for i,e in enumerate(progresses):
        remain.append((100-e+speeds[i]-1)//speeds[i])
   
    index=0
    while(1):
        if index>len(remain)-1:
            break
        for i,e in enumerate(remain):
            remain[i]-=1
        count=0

        while(index<=len(remain)-1 and remain[index]<=0):
            count+=1
            index+=1
            
        if count>0:
            answer.append(count)
        
            
    return answer

'''
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
'''
