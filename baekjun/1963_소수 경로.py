#https://www.acmicpc.net/problem/1963

from collections import deque

def cp(num):
    if num==1:
        return False

    for i in range(2,num):
        if num%i==0:
            return False

    return True

prime = [1] * 10001
for i in range(10001):
    if cp(i)==False:
        prime[i]=0


def bfs(a,b):
    q = deque()
    v = []
    q.append((a,0))
    v.append(a)

    while q:
        cur, cnt= q.popleft()
        if cur==b:
            print(cnt)
            return

        sc=str(cur)
        for i in range(1,10):
            temp=str(i)+sc[1:]
            tempNum=int(temp)
            if prime[tempNum] and tempNum not in v:
                v.append(tempNum)
                q.append((tempNum,cnt+1))

        for i in range(0,10):
            temp=sc[0]+str(i)+sc[2:]
            tempNum=int(temp)
            if prime[tempNum] and tempNum not in v:
                v.append(tempNum)
                q.append((tempNum,cnt+1))

        for i in range(0,10):
            temp=sc[:2]+str(i)+sc[3]
            tempNum=int(temp)
            if prime[tempNum] and tempNum not in v:
                v.append(tempNum)
                q.append((tempNum,cnt+1))

        for i in range(0,10):
            temp=sc[:3]+str(i)
            tempNum=int(temp)
            if prime[tempNum] and tempNum not in v:
                v.append(tempNum)
                q.append((tempNum,cnt+1))

    print(0)
    return

t=int(input())
for i in range(t):
    a, b = map(int,input().split())
    bfs(a,b)
