#https://www.acmicpc.net/problem/1932

import sys

a=int(sys.stdin.readline())
l=[]
for i in range(0,a):
    b=list(map(int,(input().split(' '))))
    l.append(b)

for i in range(1,a):
    for j in range(len(l[i])):
        if j==0:
            l[i][j]+=l[i-1][0]
        elif j==len(l[i])-1:
            l[i][j]+=l[i-1][-1]
        else:
            l[i][j]+=max(l[i-1][j-1], l[i-1][j])

print(max(l[-1]))