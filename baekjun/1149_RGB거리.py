#https://www.acmicpc.net/problem/1149

import sys

a=int(sys.stdin.readline())
m1=[[0]*3 for _ in range(1001)]
m2=[[0]*3 for _ in range(1001)]
for i in range(1,a+1):
    m1[i][0], m1[i][1], m1[i][2] =map(int,(sys.stdin.readline().split(' ')))

m2[1]=m1[1]
for i in range(2, a + 1):
    m2[i][0]=m1[i][0]+min(m2[i-1][1],m2[i-1][2])
    m2[i][1]=m1[i][1]+min(m2[i-1][0],m2[i-1][2])
    m2[i][2]=m1[i][2]+min(m2[i-1][1],m2[i-1][0])

print(min(m2[a]))
