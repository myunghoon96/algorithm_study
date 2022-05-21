import math

n, m, k = 5, 8, 3
nums = [2, 4, 5, 4, 6]

nums.sort()
ans = 0

unit = k + 1
unit_sum = k*nums[-1] + nums[-2]

ans = unit_sum*(m//unit) + nums[-1]*(m-unit*(m//unit))

print(ans)