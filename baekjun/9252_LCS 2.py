#https://www.acmicpc.net/problem/9252
#pypy3
import sys
input = sys.stdin.readline

s1=input().rstrip()
s2=input().rstrip()

mat=[['']*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            mat[i][j] = mat[i-1][j-1] + s1[i-1]
        else:
            if len(mat[i-1][j]) >= len(mat[i][j-1]):
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i][j-1]

if len(mat[-1][-1]) == 0:
    print(0)
else:
    print(len(mat[-1][-1]))
    print(mat[-1][-1])
