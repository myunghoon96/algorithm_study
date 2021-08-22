#https://programmers.co.kr/learn/courses/30/lessons/43163#

def solution(begin, target, words):
    answer = 0
    from collections import deque
    def check(w1, w2):
        diff=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                diff+=1

        if diff==1:
            return True
        return False
    
    def bfs():
        q=deque()
        q.append([begin,0])
        visited=set()
        while q:            
            b,cnt=q.pop()
            if b==target:
                return cnt
            
            for e in words:
                if e not in visited and check(b,e)==True:
                    visited.add(e)
                    q.append([e,cnt+1])
                    
        return 0

    answer=bfs()
    
    return answer