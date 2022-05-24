# https://www.acmicpc.net/problem/14888

N = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_ans = -1 * int(1e9)
min_ans = int(1e9)

def dfs(tmp_sum, idx, plus, minus, multi, divide):
    global max_ans, min_ans

    if idx + 1 == N:
        max_ans = max(max_ans, tmp_sum)
        min_ans = min(min_ans, tmp_sum)
        return
    num = nums[idx+1]

    if plus > 0:
        dfs(tmp_sum + num, idx + 1, plus - 1, minus, multi, divide)
    if minus > 0:
        dfs(tmp_sum - num, idx + 1, plus, minus - 1, multi, divide)
    if multi > 0:
        dfs(tmp_sum * num, idx + 1, plus, minus, multi - 1, divide)
    if divide > 0:
        if tmp_sum < 0:
            dfs((-1 * (abs(tmp_sum) // num)), idx + 1, plus, minus, multi, divide - 1)
        else:
            dfs(tmp_sum // num, idx + 1, plus, minus, multi, divide - 1)
    return

dfs(nums[0], 0, operations[0], operations[1], operations[2], operations[3])

print(max_ans)
print(min_ans)
