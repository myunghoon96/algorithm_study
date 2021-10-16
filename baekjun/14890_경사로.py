#https://www.acmicpc.net/problem/14890

import sys

n, l = map(int, sys.stdin.readline().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
trans_mat = list(zip(*mat))

def check(numbers):
    installed = []
    if len(set(numbers))==1:
        return True

    for i in range(n-1):
        if numbers[i]!=numbers[i+1]:
            if abs(numbers[i]-numbers[i+1])>1:
                return False
            elif numbers[i]>numbers[i+1]:
                if i+1+l>n:
                    return False
                for position in range(i+1,i+1+l):
                    if position in installed:
                        return False
                for position in range(i+1,i+1+l):
                    installed.append(position)
            elif numbers[i]<numbers[i+1]:
                if i+1-l<0:
                    return False
                for position in range(i+1-l,i+1):
                    if position in installed:
                        return False

                for position in range(i+1-l,i+1):
                    installed.append(position)

    return True

ans = 0
for i in range(n):
    if check(mat[i]):
        # print("row ", i, "success")
        ans+=1

for i in range(n):
    if check(trans_mat[i]):
        # print("col ", i, "success")
        ans+=1
print(ans)