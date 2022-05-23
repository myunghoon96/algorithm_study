# https://www.acmicpc.net/problem/1715
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

# if n == 1:
#     print(cards[0])
#     exit(0)

ans = 0
while len(cards) >= 2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    ans += (a+b)
    heapq.heappush(cards, a+b)

print(ans) 