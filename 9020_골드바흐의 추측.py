#https://www.acmicpc.net/problem/9020

def checkPrime(num):
    if num==1:
        return 0

    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1

tempL=[]
for i in range(2,10001):
    if checkPrime(i):
        tempL.append(i)

t=int(input())


for i in range(t):
    a=int(input())

    b=a//2
    c=a//2

    while(1):
        if b in tempL and c in tempL:
            if b+c==a:
                print(b,c)
                break
        b-=1
        c+=1

