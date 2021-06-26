#https://www.acmicpc.net/problem/2156

a=int(input())
l=[0 for _ in range(a+2)]
m=[0 for _ in range(a+2)]
for i in range(1,a+1):
    l[i]=int(input())

m[1]=l[1]
m[2]=l[1]+l[2]

for i in range(3,a+1):
    m[i]=max(m[i-1],m[i-2]+l[i],m[i-3]+l[i-1]+l[i])

print(m[a])