#https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    
    left=0
    right=distance
    rocks.sort()
    while left<=right:
        
        mid = (left+right)//2
        #previous stone position
        pre=0
        remove=0
        minD=1000000001
        for r in rocks:
            d=r-pre
            if d<mid:
                remove+=1
            else:
                pre=r
                minD=min(d,minD)

        #because remove too many stone, mid have to be smaller
        if remove>n:
            right=mid-1
        else:
            left=mid+1
            answer=minD
            
    return answer