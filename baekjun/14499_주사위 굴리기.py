#https://www.acmicpc.net/problem/14499
import sys
n,m,x,y,k = map(int, sys.stdin.readline().split())
matrix = []
dice = dict()
dice['up']=0
dice['down']=0
dice['north']=0
dice['west']=0
dice['east']=0
dice['south']=0
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

instructions=list(map(int, sys.stdin.readline().split()))
def move(ins):
    global x,y,matrix,dice
    index=ins-1
    if x+dx[index]>=n or x+dx[index]<0:
        return
    if y+dy[index]>=m or y+dy[index]<0:
        return
    x=x+dx[index]
    y=y+dy[index]

    if ins == 1: #east
        temp=dice['east']
        dice['east']=dice['up']
        dice['up']=dice['west']
        dice['west']=dice['down']
        if matrix[x][y]==0:
            matrix[x][y]=temp
            dice['down']=matrix[x][y]
        else:
            dice['down']=matrix[x][y]
            matrix[x][y]=0
    elif ins == 2: #west
        temp = dice['west']
        dice['west']=dice['up']
        dice['up']=dice['east']
        dice['east']=dice['down']
        if matrix[x][y]==0:
            matrix[x][y]=temp
            dice['down']=matrix[x][y]
        else:
            dice['down']=matrix[x][y]
            matrix[x][y]=0
    elif ins == 3: #north
        temp = dice['north']
        dice['north']=dice['up']
        dice['up']=dice['south']
        dice['south']=dice['down']
        if matrix[x][y]==0:
            matrix[x][y]=temp
            dice['down']=matrix[x][y]
        else:
            dice['down']=matrix[x][y]
            matrix[x][y]=0
    elif ins == 4: #south
        temp = dice['south']
        dice['south']=dice['up']
        dice['up']=dice['north']
        dice['north']=dice['down']
        if matrix[x][y]==0:
            matrix[x][y]=temp
            dice['down']=matrix[x][y]
        else:
            dice['down']=matrix[x][y]
            matrix[x][y]=0
    
    print(dice['up'])

for ins in instructions:
    move(ins)
    
