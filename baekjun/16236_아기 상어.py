#https://www.acmicpc.net/problem/16236

import sys
from collections import deque

N = int(sys.stdin.readline())
matrix=[]

ans_time=0
shark_size=2
shark_feed=0

for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    matrix.append(temp)
    for j in range(N):
        if temp[j]==9:
            shark_x,shark_y=i,j

#find nearest fish that fish_size<shark_size
def bfs():
    global shark_size
    global shark_feed
    global ans_time
    global shark_x
    global shark_y

    origin_x,origin_y=shark_x,shark_y
    q=deque()
    visit=[[0 for _ in range(N)] for _ in range(N)]  
    visit[origin_x][origin_y]=1   
    q.append((origin_x,origin_y,0))
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    possible_fish=[]
    while q:
           
        sx,sy,cnt=q.popleft()
  
        for i in range(4):
            sxx=sx+dx[i]
            syy=sy+dy[i]

            #move
            if 0<=sxx<N and 0<=syy<N and visit[sxx][syy]==0 and shark_size>=matrix[sxx][syy]:
                visit[sxx][syy]=1
                q.append((sxx,syy,cnt+1))
                #possible eat
                if 1<=matrix[sxx][syy]<=6 and shark_size>matrix[sxx][syy]:
                    possible_fish.append((sxx,syy,cnt+1))



    if len(possible_fish)>0:
        possible_fish.sort(key = lambda x : (x[2], x[0], x[1]))
        # print("nearest possible eat fish ", possible_fish)
        # print()
        eat_x,eat_y,eat_cnt=possible_fish[0]
        matrix[eat_x][eat_y]=9
        matrix[origin_x][origin_y]=0

        shark_feed+=1
        ans_time+=eat_cnt
        if shark_size==shark_feed:
            shark_feed=0
            shark_size+=1

        shark_x=eat_x
        shark_y=eat_y

        return 1


    return -1
    
while (1):
    if bfs()==-1:
        break

print(ans_time)

