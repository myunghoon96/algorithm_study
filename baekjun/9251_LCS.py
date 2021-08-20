#https://www.acmicpc.net/problem/9251

s1=input()
s2=input()

mat=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1]==s2[j-1]:
            mat[i][j]=mat[i-1][j-1]+1
        else:
            mat[i][j]=max(mat[i-1][j],mat[i][j-1])

ans=0
for r in mat:
    ans=max(ans,max(r))

print(ans)
