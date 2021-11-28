#https://www.acmicpc.net/problem/13458

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

ans = 0

for people in a:
    ans+=1
    
    if people > b:
        ans+=(people-b)//c
        if (people-b)%c!=0:
            ans+=1

print(int(ans))