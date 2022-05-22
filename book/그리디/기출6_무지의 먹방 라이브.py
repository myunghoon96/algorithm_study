def solution(food_times, k):
    answer = 0
    
    idx = 0
    zero_cnt = 0
    while k > 0:
        if food_times[idx] > 0:
            food_times[idx] -= 1
            k -= 1
            if food_times[idx] == 0:
                zero_cnt += 1
                if zero_cnt == len(food_times):
                    return -1
        # print(food_times)
        # print(idx)
        # print(zero_cnt)
        idx += 1
        if idx == len(food_times):
            idx = 0
    return idx+1