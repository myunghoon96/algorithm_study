#https://www.acmicpc.net/problem/1747

n=int(input())

def cp(num):
    if num==1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False

    return True

def pl(num):
    temp=str(num)
    temp2=temp[::-1]

    if temp==temp2:
        return True

    return False

while 1:
    status=cp(n)
    status2=pl(n)
    
    if status and status2:
        break

    else:
        n+=1

print(n)