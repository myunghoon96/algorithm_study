#https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0 for _ in range(target+1)]

        for i in range(target+1):
            for num in nums:
                if i>num:
                    dp[i]+=dp[i-num]
                elif i==num:
                    dp[i]+=1
                else:
                    continue
                
        # print(dp)
        return dp[target]
    
#         def combinationSum4(self, nums: List[int], target: int) -> int:
#         ans=0
#         for i in range(2, target+1):
#             l = list(product(nums, repeat=i))

#             for e in l:
#                 if sum(e) == target:
#                     # print(e)
#                     ans+=1
        
#         return ans