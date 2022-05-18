# https://www.acmicpc.net/problem/2531
from collections import deque
n, d, k, c = map(int, (input().split()))
foods = [int(input()) for _ in range(n)]
#원형 테이블
foods.extend(foods[:k-1])

r = 0
q = deque()
ans = 0
while r < len(foods):
    q.append(foods[r])
    r+=1
    if len(q) > k:
        q.popleft()

    if len(q) == k:
        ans = max(ans, len((set(q).union(set([c])))))  
print(ans)