#https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        
        dp1=[0 for _ in range(len(nums))]
        dp2=[0 for _ in range(len(nums))]

        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])
        
        for i in range(2, len(nums)-1):
            dp1[i]=max(dp1[i-1], dp1[i-2]+nums[i])
        
        for i in range(3, len(nums)):
            dp2[i]=max(dp2[i-1], dp2[i-2]+nums[i])
        
        # print(dp1)
        # print(dp2)
        return max(max(dp1),max(dp2))