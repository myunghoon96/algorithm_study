# https://www.acmicpc.net/problem/2504

import sys

input_str = sys.stdin.readline().rstrip()

stack = []
not_correct_flag = False

ttl_score = 0
tmp_score = 1
for i in range(len(input_str)):
    char = input_str[i]

    if char == '(':
        stack.append(char)
        tmp_score *= 2

    elif char == '[':
        stack.append(char)
        tmp_score *= 3

    elif char == ')' or char == ']':
        if len(stack) <= 0:
            not_correct_flag = True
            break

        if len(stack) > 0 :
            last_char = stack.pop()
            if (char == ')' and last_char != '(') or (char == ']' and last_char != '['):
                not_correct_flag = True
                break
        
        if i - 1 >= 0:
            pre_char = input_str[i-1]
            if char == ')' and pre_char == '(':
                ttl_score += tmp_score
                
            elif char == ']' and pre_char == '[':
                ttl_score += tmp_score

        if char == ')':
            tmp_score //= 2
        elif char == ']':
            tmp_score //= 3
            
if not_correct_flag or len(stack) > 0:
    print(0)
else:
    print(ttl_score)