#https://www.acmicpc.net/problem/14888

import sys
input=sys.stdin.readline

n=int(input())
nl=list(map(int,input().split(' ')))
op=list(map(int,input().split(' ')))

minA=1000000001
maxA=-1000000001


def f(idx,num,plus,minus,multi,division):
    global n, minA, maxA
    if idx==n-1:
        minA=min(minA,num)
        maxA = max(maxA, num)
        return
    if plus:
        f(idx+1, num+nl[idx+1], plus-1, minus, multi, division)
    if minus:
        f(idx+1, num-nl[idx+1], plus, minus-1, multi, division)
    if multi:
        f(idx+1, num*nl[idx+1], plus, minus, multi-1, division)
    if division:
        f(idx+1, int(num/nl[idx+1]), plus, minus, multi, division-1)

f(0,nl[0],op[0],op[1],op[2],op[3])

print(maxA)
print(minA)
