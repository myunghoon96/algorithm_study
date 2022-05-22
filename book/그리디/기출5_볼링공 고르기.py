from itertools import combinations

n, m = 5, 3
balls = [1, 3, 2, 3, 2]

# n, m = 8, 5
# balls = [1, 5, 4, 3, 2, 4, 5, 2]

combis = combinations(balls, 2)

ans = 0
for combi in combis:
    if combi[0] != combi[1]:
        ans += 1

print(ans)