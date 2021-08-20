#https://www.acmicpc.net/problem/2565

a=int(input())
dp=[1 for i in range(501)]
l=[]
for i in range(a):
    pair=list(map(int,(input().split(' '))))
    l.append(pair)

l.sort(key=lambda x:(x[0],x[1]))

for i in range(1,a):
    for j in range(i):
        if l[i][1]>l[j][1]:
            dp[i]=max(dp[j]+1,dp[i])

print(a-max(dp))