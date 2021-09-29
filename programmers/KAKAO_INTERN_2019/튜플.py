#https://programmers.co.kr/learn/courses/30/lessons/64065

from collections import Counter
def solution(s):
    answer = []
    
    temp = s.replace('{','').replace('}','').split(',')
    counter = Counter(temp)
    # print(counter)
    for key, cnt in counter.most_common():
        answer.append(int(key))
    
    return answer