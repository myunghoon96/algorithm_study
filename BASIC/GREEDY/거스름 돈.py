money = 660

coins = [500, 100, 50, 10]

ans = 0
for coin in coins:
    ans += money//coin
    money%=coin

print(ans)