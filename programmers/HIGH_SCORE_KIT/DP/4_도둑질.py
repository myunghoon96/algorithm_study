#https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0
    
    if len(money)==0:
        return 0
    elif len(money)<=3:
        return max(money)
       
    #NOT steal last house, steal first house
    dp = [0 for _ in range(len(money))]
    dp[0]=money[0]
    dp[1]=money[0]
    for i in range(2, len(money)-1):
        dp[i]=max(money[i]+dp[i-2], dp[i-1])

    #NOT steal first house, steal last house
    dp2 = [0 for _ in range(len(money))]
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2, len(money)):
        dp2[i]=max(money[i]+dp2[i-2], dp2[i-1])

    answer=max(max(dp), max(dp2))
    return answer