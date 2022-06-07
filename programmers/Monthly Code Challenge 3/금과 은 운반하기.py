# https://programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    answer = int(10**9)*int(10**5)*2*2
    
    left, right = 0, int(10**9)*int(10**5)*2*2
    
    while left <= right:
        mid = (left + right) //2
        hours = mid
        ttl_gold = 0
        ttl_silver = 0
        ttl_weight = 0
        
        for i in range(len(g)):
            one_time = t[i]
            one_weight = w[i]
            golds = g[i]
            silvers = s[i]

            city_times = hours//(one_time*2)
            if hours%(one_time*2) >= one_time:
                city_times += 1
            
            if one_weight * city_times < golds:
                city_max_golds = one_weight * city_times
            else:
                city_max_golds = golds
                
            if one_weight * city_times < silvers:
                city_max_silvers = one_weight * city_times
            else:
                city_max_silvers = silvers
    
            if one_weight * city_times < golds + silvers:
                city_max_weights = one_weight * city_times
            else:
                city_max_weights = golds + silvers
                
            ttl_gold += city_max_golds
            ttl_silver += city_max_silvers
            ttl_weight += city_max_weights
            
        if ttl_gold >= a and ttl_silver >= b and ttl_weight >= a + b:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
            
    return answer