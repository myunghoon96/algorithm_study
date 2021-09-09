#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        mindp=[0 for _ in range(len(nums))]
        maxdp=[0 for _ in range(len(nums))]

        mindp[0]=nums[0]
        maxdp[0]=nums[0]

        for i in range(1, len(nums)):
            maxdp[i]=max(nums[i], max(mindp[i-1]*nums[i], maxdp[i-1]*nums[i]))
            mindp[i]=min(nums[i], min(mindp[i-1]*nums[i], maxdp[i-1]*nums[i]))

        # print(maxdp)
        # print(mindp)
      
        return max(maxdp)