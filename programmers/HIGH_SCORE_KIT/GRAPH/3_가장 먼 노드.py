#https://programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    from collections import deque
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visit=[-1 for _ in range(n+1)]
    visit[1]=0
    
    def bfs():
        q=deque()
        q.append((1,0))

        while q:
            x,cnt = q.popleft()

            for n in graph[x]:
                if visit[n]==-1:
                    q.append((n,cnt+1))
                    visit[n]=cnt+1
                    
        return visit
    
    result = bfs()
    
    maxResult=max(result)
    for e in result:
        if e==maxResult:
            answer+=1
            
    return answer