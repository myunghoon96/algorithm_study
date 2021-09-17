#https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    
    l=1
    r=200000000
    while l<=r:
        mid=(l+r)//2
        blank=0
        for stone in stones:
            if stone<=mid:
                blank+=1 
            else:
                blank=0
                
            if blank>=k:
                break
        
        if blank>=k:
            r=mid-1
        else:
            l=mid+1
        
    
    return l