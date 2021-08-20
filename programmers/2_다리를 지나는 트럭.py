#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight=0
    cur_length=0
    cur_bridge=[]
    cycle=1
    
    tempIndex=0
    
    while 1:

        cycle+=1
        
        if len(truck_weights)>0:
            w = truck_weights[0]
            if cur_length<bridge_length and cur_weight+w<=weight:
                w=truck_weights.pop(0)
                cur_length+=1
                cur_weight+=w
                cur_bridge.append([w,0])
        
        
        for i in range(tempIndex, len(cur_bridge)):
            cur_bridge[i][1]+=1
            if cur_bridge[i][1]==bridge_length:
                cur_length-=1
                cur_weight-=cur_bridge[i][0]
                tempIndex+=1
                # print(cycle, cur_bridge[i][0])
                
        if len(truck_weights)==0 and cur_bridge[-1][1]==bridge_length:
            # print (cycle)
            return cycle
                