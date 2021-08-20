#https://www.acmicpc.net/problem/2580

l=[]
for i in range(9):
    temp=list(map(int, input().split()))
    l.append(temp)

l2=[]
for i in range(9):
    for j in range(9):
        if l[i][j]==0:
            pair=[i,j]
            l2.append(pair)

total=len(l2)

def c(x,y):
    can=[1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(0,9):
        if l[x][i] in can:
            can.remove(l[x][i])
        if l[i][y] in can:
            can.remove(l[i][y])

    dx=(x//3)*3
    dy=(y//3)*3
    for r in range(dx, dx+3):
        for c in range(dy, dy+3):
            if l[r][c] in can:
                can.remove(l[r][c])

    return can

flag=False
def f(cnt):
    global flag

    if flag==True:
        return

    if cnt==total:
        for i in range(9):
            for j in range(9):
                print(l[i][j], end=" ")
            print()
        flag=True
        return

    temp=l2[cnt]
    x=temp[0]
    y=temp[1]

    for num in c(x,y):
        l[x][y]=num
        f(cnt+1)
        l[x][y]=0

f(0)