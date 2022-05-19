# https://programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    basic_time, basic_fee, extra_time, extra_fee = fees
    time_dic = defaultdict(list)
    ttl_time_dic = defaultdict(int)
    fee_dic = defaultdict(int)
    
    # print(basic_time, basic_fee, extra_time, extra_fee)
    for record in records:
        time, car, kind = record.split()
        minutes = int(time.split(':')[0])*60 + int(time.split(':')[1]) 
        # print(time, minutes, car, kind)
        time_dic[car].append(minutes)
        
    for k, v in time_dic.items():
        if len(v) % 2 != 0:
            time_dic[k].append(23*60+59)
    # print(time_dic)
    
    for car, times in time_dic.items():
        total_time = 0
        for i in range(0, len(times), 2):
            use_time = times[i+1] - times[i]
            total_time += use_time
        ttl_time_dic[car] = total_time
    # print(ttl_time_dic)
    
    for car, ttl_time in ttl_time_dic.items():
        if ttl_time <= basic_time:
            fee_dic[car] = basic_fee
        else:
            fee_dic[car] = basic_fee + math.ceil((ttl_time - basic_time)/extra_time) * extra_fee
    
    # print(fee_dic)
    sorted_list = sorted(fee_dic.items())
    # print(sorted_list)
    for k,v in sorted_list:
        answer.append(v)    
    return answer