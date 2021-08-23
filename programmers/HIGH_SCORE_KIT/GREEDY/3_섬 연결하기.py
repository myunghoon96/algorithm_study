#https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0

    costs.sort(key = lambda x:x[2])
    
    graph=set()
    graph.add(costs[0][0])

    while True:
        if len(graph)==n:
            break
        for a,b,c in costs:
            if a in graph and b in graph:
                continue
            if a in graph or b in graph:
                graph.add(a)
                graph.add(b)
                answer+=c
                break
    return answer