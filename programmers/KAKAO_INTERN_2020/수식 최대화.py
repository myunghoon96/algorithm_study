#https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
def calculate(op_list, expression):
    op1, op2, op3 = op_list
    first = expression.split(op1)
    second = [f.split(op2) for f in first]

    third = []
    for s in second:
        temp=''
        for i,e in enumerate(s):
            e='('+e+')'
            temp+=str(e)
            if i != len(s)-1:
                temp+=op2
        third.append(temp)

    for i in range(len(third)):
        third[i]='('+third[i]+')'

    result = op1.join(third)
    # print(result)
    # print(abs(eval(result)))
    return abs(eval(result))
def solution(expression):
    answer = 0
    ansList = []
    permu = list(permutations(['+', '-', '*'], 3))
    
    for per in permu:
        result = calculate(per, expression)
        ansList.append(result)
    
    answer = max(ansList)
    return answer