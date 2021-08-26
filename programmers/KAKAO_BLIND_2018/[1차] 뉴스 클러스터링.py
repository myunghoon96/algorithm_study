#https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter
def solution(str1, str2):
    answer = 0

    l1=[]
    l2=[]
    for i in range(len(str1)-1):
        temp=str1[i]+str1[i+1]
        if temp.isalpha():
            l1.append(temp.lower())
    
    for i in range(len(str2)-1):
        temp=str2[i]+str2[i+1]
        if temp.isalpha():
            l2.append(temp.lower())
    
    c1 = Counter(l1)
    c2 = Counter(l2)
    intersect_c=c1 & c2
    union_c = c1 | c2

    inter = len(list(intersect_c.elements()))
    uni = len(list(union_c.elements()))

    if uni==0:
         return 1*65536
    
    else:
        return int(inter/uni*65536)
    