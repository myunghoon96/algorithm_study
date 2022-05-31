# https://www.acmicpc.net/problem/17298


N = int(input())
nums = list(map(int, input().split()))

ans = [-1] * N
stack = []
for idx, num in enumerate(nums):

    while stack:
        last_idx, last_num = stack[-1]
        if num > last_num:
            stack.pop()
            ans[last_idx] = num
        elif num <= last_num:
            break
        
    stack.append((idx, num))
print(*ans)
