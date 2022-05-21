n = 4
foods = [1, 3, 1, 5]

# dp = [0] * (n)
# dp[0] = foods[0]
# dp[1] = foods[0]
# #steal zero idx, not steal first idx
# for i in range(2, n):
#     dp[i] = max(dp[i-1], dp[i-2]+foods[i]) 
# print(dp)
# dp2 = [0] * (n)
# dp2[1] = foods[1]
# dp2[2] = foods[1]
# #steal zero idx, not steal first idx
# for i in range(3, n):
#     dp2[i] = max(dp2[i-1], dp2[i-2]+foods[i]) 
# print(dp2)
# print(max(dp[-1], dp2[-1]))

dp3 = [0] * (n)
dp3[0] = foods[0]
dp3[1] = max(foods[0], foods[1])
for i in range(2, n):
    dp3[i] = max(dp3[i-1], dp3[i-2]+foods[i]) 
print(dp3[-1])
