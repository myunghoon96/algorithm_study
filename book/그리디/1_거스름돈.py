n = 1260
coins = [500, 100, 50, 10]
idx = 0
ans = 0

while idx < len(coins):
    coin = coins[idx]
    ans += n // coin
    n = n % coin
    idx += 1

print(ans)

#or use for ... in ...
