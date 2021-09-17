#https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import permutations
def check(ban_list, user_list):
    
    for i in range(len(ban_list)):
        if len(ban_list[i]) != len(user_list[i]):
            return False
        if re.match(ban_list[i], user_list[i]) == None:
            return False
    
    return True

def solution(user_id, banned_id):
    answer = 0
    ban_list = [ban.replace('*','.') for ban in banned_id]
    permu = permutations(user_id, len(banned_id))
    ansSet = set()
    for user_list in permu:
        if check(ban_list, user_list):
            users = sorted(list(user_list))
            users = tuple(users)
            ansSet.add(users)
            
    answer = len(ansSet)    
    return answer