#https://www.acmicpc.net/problem/17281

import sys
from itertools import permutations
n=int(sys.stdin.readline())
players = [i for i in range(1,9)]
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = -1
def play(select):
    global ans
    idx=0
    score=0
    for inning in innings:
        out=0
        b1,b2,b3=0,0,0
        while out<3:
            if inning[select[idx]] == 0:
                out+=1
            elif inning[select[idx]] == 1:
                score += b3    
                b1,b2,b3=1,b1,b2
            elif inning[select[idx]] == 2:
                score += (b2+b3)    
                b1,b2,b3=0,1,b1
            elif inning[select[idx]] == 3:
                score += (b1+b2+b3)    
                b1,b2,b3=0,0,1
            elif inning[select[idx]] == 4:
                score += (b1+b2+b3+1)    
                b1,b2,b3=0,0,0

            idx+=1
            if idx==9:
                idx=0
    if score>ans:
        ans=score 

permu = permutations(players,8)
for p in permu:
    p=list(p)
    select=p[:3]+[0]+p[3:]
    play(select)
print(ans)


