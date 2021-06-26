#https://www.acmicpc.net/problem/11054

n = int(input())
l = list(map(int, input().split()))
lr= l[::-1]

dp=[1 for _ in range(n)]
dp2=[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if l[i]>l[j]:
            dp[i]=max(dp[i], dp[j]+1)
        if lr[i]>lr[j]:
            dp2[i]=max(dp2[i], dp2[j]+1)

ans=0
for i in range(n):
    ans=max(ans,(dp[i]+dp2[n-1-i]))
print(ans-1)