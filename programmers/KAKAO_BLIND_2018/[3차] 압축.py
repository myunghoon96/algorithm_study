#https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    d=dict()
    for i in range(1,27):
        d[chr(64+i)]=i
    
    i=0
    ans=0
    while i < len(msg):
        cur=""
        cnt=0
        org_i=i
        
        while True:
            if org_i + cnt >= len(msg):
                break

            cur += msg[org_i+cnt]
            
            if cur in d.keys():
                # print("IN ", cur)
                cnt+=1
                i+=1
                ans=d[cur]
            
            if cur not in d.keys():
                # print("NOT IN ", cur)
                d[cur]=len(d.keys())+1
                answer.append(ans)
                break
    answer.append(ans)    
            
    # print(d)      

    return answer