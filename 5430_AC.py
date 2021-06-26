#https://www.acmicpc.net/problem/5430

import sys
from collections import deque

num=int(input())

for i in range(num):

    ins=input()
    n = int(input())
    arr = input()
    l = deque()

    rStatus=False


    if n==0:
        arr=[]
    else:
        arr=arr[1:-1].split(',')

    for e in arr:
        l.append(int(e))

    if len(l)<ins.count('D'):
        print("error")
        continue

    for e in ins:
        if e=='R':
            if rStatus==True:
                rStatus=False
            else:
                rStatus=True
        elif e=='D':
            if rStatus==True:
                l.pop()
            else:
                l.popleft()


    answer=[]
    if rStatus==False:
        answer=l
    else:
        answer=list(reversed(l))

    print("[", end='')
    for i in range(len(answer)):
        if i == len(answer) - 1:
            print(answer[i], end = '')
        else:
            print("%s," %(answer[i]), end='')
    print("]")
