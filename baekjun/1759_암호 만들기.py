# https://www.acmicpc.net/problem/1759
from itertools import combinations

L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()

def check(input_string):
    aeiou_cnt = 0
    other_cnt = 0

    for i in range(len(input_string)):
        if input_string[i] in ['a', 'e', 'i', 'o', 'u']:
            aeiou_cnt += 1
        else:
            other_cnt += 1

    if aeiou_cnt >=1 and other_cnt >=2:
        return True
    
    return  False

combis = list(combinations(alphas, L))
for combi in combis:
    tmp_str = ''.join(combi)
    if check(tmp_str):
        print(tmp_str)
    