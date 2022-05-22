from itertools import combinations

n = 5
coins = [3, 2, 1, 1, 9]

# n = 3
# coins = [3, 5, 7]

coins.sort()

candidates = set()
for i in range(1, len(coins)+1):
    combis = combinations(coins, i)
    for combi in combis:
        candidates.add(sum(combi))

print(candidates)

money = 1
while True:
    if money in candidates:
        money += 1
    else:
        print(money)
        break