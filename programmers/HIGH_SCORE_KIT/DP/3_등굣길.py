#https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    row=n
    col=m
    
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
  
    dp[1][1]=1
    
    for i in range(1,row+1):
        for j in range(1,col+1):
            if i==1 and j==1:
                continue

            if [j,i] not in puddles:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
  
    answer=dp[-1][-1]%1000000007
    return answer