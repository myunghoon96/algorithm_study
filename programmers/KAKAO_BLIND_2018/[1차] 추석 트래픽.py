#https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    answer = 0
    start=[]
    end=[]
    
    def time(a):
        d,t,e =a.split(' ')        
        h=int(t[0:2])*3600*1000
        m=int(t[3:5])*60*1000
        s=int(t[6:8])*1000
        ms=int(t[9:12])
        ex=int(float(e[:-1])*1000)
           
        right=h+m+s+ms
        left=right-ex+1               
        end.append(right)
        start.append(left)
        
    for i,e in enumerate(lines):
        time(e)
    
    for i in range(len(end)):
        cnt=0
        for j in range(i, len(start)):
            if end[i]+1000>start[j]:
                cnt+=1
            
        answer=max(answer,cnt)
    
    
    
    return answer