# https://www.acmicpc.net/problem/7662
import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    max_q = []
    min_q = []
    deleted = [False] * K

    for i in range(K):
        oper, num = sys.stdin.readline().split()
        num = int(num)

        if oper == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            
        elif oper == 'D':
            if num == 1:
                while max_q and deleted[max_q[0][1]]:
                    heapq.heappop(max_q)

                if max_q:
                    max_num, max_idx = heapq.heappop(max_q)
                    deleted[max_idx] = True
                
            elif num == -1:
                while min_q and deleted[min_q[0][1]]:
                    heapq.heappop(min_q)
   
                if min_q:
                    min_num, min_idx = heapq.heappop(min_q)
                    deleted[min_idx] = True

    
    while max_q and deleted[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and deleted[min_q[0][1]]:
        heapq.heappop(min_q)

    if max_q and min_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print("EMPTY")