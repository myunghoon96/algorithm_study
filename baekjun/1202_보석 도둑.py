# https://www.acmicpc.net/problem/1202
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewls = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = list(int(sys.stdin.readline().rstrip()) for _ in range(K))

bags.sort()
jewls.sort()

ans = 0
can_taken = []
for bag in bags:
    if not jewls and not can_taken:
        break

    while jewls and bag >= jewls[0][0]:
        m, v = heapq.heappop(jewls)
        heapq.heappush(can_taken, -v)
    
    if len(can_taken) > 0:
        max_val_in_can_taken = heapq.heappop(can_taken)
        ans += (-1 * max_val_in_can_taken)
    
print(ans)