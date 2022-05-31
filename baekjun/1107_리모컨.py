# https://www.acmicpc.net/problem/1107

N = int(input())
M = int(input())
if M > 0:
    brokens = set(list(map(int, input().split())))
else:
    brokens = set()
    
def can_make(num):
    for e in str(num):
        if int(e) in brokens:
            return False
    return True

ans = abs(N - 100)
for num in range(1000001):
    if can_make(num):
        dist = len(str(num)) + abs(N-num)
        ans = min(ans, dist)
print(ans)