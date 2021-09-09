#https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp=[10001 for _ in range(amount+1)]
        ans=0
        dp[0]=0
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i]=min(dp[i],dp[i-coin]+1)
                else:
                    break
        
        if dp[amount]==10001:
            return -1
        
        return dp[amount]
