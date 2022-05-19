# https://programmers.co.kr/learn/courses/30/lessons/92342

from collections import defaultdict

def solution(n, info):
    answer = []
    
    # print(n)
    # print(info)
    max_diff = -1
    dic = defaultdict(list)
    def dfs(p_ttl_score, l_ttl_score, idx, remain, history):
        nonlocal max_diff
        
        if idx == len(info):
            if l_ttl_score-p_ttl_score >= max_diff:
                # print(p_ttl_score, l_ttl_score, l_ttl_score-p_ttl_score)
                # print(history)
                if remain > 0:
                    history[-1] += remain
                max_diff = l_ttl_score-p_ttl_score
                dic[max_diff].append(history)    
            return
        
        p_hit = info[idx]
        if p_hit > 0:
            p_score = 10 - idx
        else:
            p_score = 0
        #lion hit more than peach
        if remain >= p_hit+1:
            dfs(p_ttl_score, l_ttl_score+(10-idx), idx+1, remain-(p_hit+1), history+[p_hit+1])
    
        #lion no hit
        dfs(p_ttl_score+p_score, l_ttl_score, idx+1, remain, history+[0])
    
        return
    dfs(0, 0, 0, n, [])
    # print(max_diff)
    # print(dic[max_diff])
    
    rev_candidates = [e[::-1] for e in dic[max_diff]]
    sorted_list = sorted(rev_candidates)
    # print(sorted_list[-1][::-1])    

    if max_diff <= 0:
        return [-1]
        
    return sorted_list[-1][::-1]
