#https://programmers.co.kr/learn/courses/30/lessons/60057#

def solution(s):
    answer = 1001
    size=1
    
    if len(s)==1:
        return 1
    
    for size in range(1,len(s)//2+1):
        l=[]
        for j in range(0, len(s), size):
            l.append(s[j:j+size])
        

        ans=0
        cnt=1
        for i in range(len(l)):         
            if i==0:
                pre=l[0]
                cnt=1
                continue
                
            cur=l[i]            
            if pre == cur:
                cnt+=1
            else:
                if cnt==1:
                    cnt=""
                ans+=len(str(cnt))+len(pre)            
                pre=cur
                cnt=1
                
        if cnt==1:
            cnt=""
        ans+=len(str(cnt))+len(pre)   

        answer=min(answer,ans)
    return answer