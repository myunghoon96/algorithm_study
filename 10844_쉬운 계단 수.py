#https://www.acmicpc.net/problem/10844

a=int(input())
m=[[0]*10 for _ in range(a+1)]

for i in range(1,10):
    m[1][i]=1

for i in range(2,a+1):
    for j in range(10):
        if j==0:
            m[i][j]=m[i-1][j+1]
        elif j==9:
            m[i][j]=m[i-1][j-1]

        else:
            m[i][j]=m[i-1][j-1]+m[i-1][j+1]

print(sum(m[a]) %1000000000)
