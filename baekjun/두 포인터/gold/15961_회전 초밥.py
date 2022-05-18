# https://www.acmicpc.net/problem/15961
#pypy3
from collections import defaultdict

n, d, k, c = map(int, input().split())
foods = [int(input()) for _ in range(n)]
foods.extend(foods[:k-1])


dic = defaultdict(int)
for i in range(k):
    dic[foods[i]] += 1
ans = len(dic)
dic[c] += 1

l, r = 0, k-1
# print(l, r, foods[l], foods[r] ,dic, len(dic))
while r < len(foods)-1:
    dic[foods[l]] -= 1
    if dic[foods[l]] == 0:
        del dic[foods[l]]
    
    l += 1
    r += 1

    dic[foods[r]] += 1
    # print(l, r, foods[l], foods[r] ,dic, len(dic))
    ans = max(ans, len(dic))
print(ans)