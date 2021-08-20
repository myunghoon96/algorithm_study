#https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville);
    count=0;
    while(scoville[0]<K): 
        if count>=1000000 or len(scoville)<2:
            answer=-1;
            break;        
        min1=heapq.heappop(scoville);
        min2=heapq.heappop(scoville);
        
        mix=min1+(min2*2);
        heapq.heappush(scoville,mix);   
        answer+=1;
        count+=1;
    # print(answer, count)
    return answer