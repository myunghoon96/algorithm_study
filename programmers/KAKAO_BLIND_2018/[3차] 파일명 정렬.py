#https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = []
    l=[]
    for index,f in enumerate(files):
        dStart=0
        dEnd=0
        for i in range(len(f)):
            if dEnd-dStart>5:
                break
                
            if dStart==0 and f[i].isdigit():
                dStart=i
                dEnd=i+1
            elif dStart!=0 and f[i].isdigit() :
                dEnd=i+1
            
            if dStart!=0 and f[i].isdigit() == False:
                break
            
        # print(dStart, dEnd, dEnd-dStart)
        
        head=f[:dStart].lower()
        number=int(f[dStart:dEnd])
        tail=f[dEnd:]
        
        # print(head, number, tail, f)
        l.append((head,number, index, f)) 
    
    l.sort(key=lambda x:(x[0],x[1],x[2]))
    # print(l)
    
    for e in l:
        answer.append(e[3])
    
    return answer