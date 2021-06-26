#https://www.acmicpc.net/problem/5052

import sys
input=sys.stdin.readline

t=int(input())

def f(nl):
    for i in range(len(nl)-1):
        if nl[i] in nl[i+1][0:len(nl[i])]:
            return False

    return True

for i in range(t):
    n=int(input())
    l=[]
    for j in range(n):
        l.append(input().strip())

    l.sort()

    if f(l):
        print("YES")
    else:
        print("NO")