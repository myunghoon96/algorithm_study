# https://www.acmicpc.net/problem/1655
# heap 2 개, left heap, right heap
import heapq
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
left_heap = []
right_heap = []

for num in nums:
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * num)
    else:
        heapq.heappush(right_heap, num)
    
    if len(left_heap) > 0 and len(right_heap) > 0 and (-1 * left_heap[0]) > right_heap[0]:
        max_num_in_left_heap = heapq.heappop(left_heap)
        min_num_in_right_heap = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -1 * min_num_in_right_heap)
        heapq.heappush(right_heap, -1 * max_num_in_left_heap)
    
    print(-1 * left_heap[0])
