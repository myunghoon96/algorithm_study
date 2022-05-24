# https://www.acmicpc.net/problem/2110
import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
homes = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
homes.sort()

l, r = 1, homes[-1]-homes[0]
ans = 0
# print(homes)
while l <= r:
    mid_dist = (l + r) // 2
    
    tmp_dist = 0
    install_cnt = 1

    for i in range(1, N):
        tmp_dist += (homes[i] - homes[i-1])
        if tmp_dist >= mid_dist:
            install_cnt += 1
            tmp_dist = 0
        
   
    if install_cnt >= C:
        ans = max(ans, mid_dist)
        l = mid_dist + 1
    
    elif install_cnt < C:
        r = mid_dist - 1
        
print(ans)