#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            
            while left < right:
                if nums[left]+nums[right]+nums[i] < 0:
                    left+=1
                elif nums[left]+nums[right]+nums[i] > 0:
                    right-=1
                elif nums[left]+nums[right]+nums[i] == 0:
                    ans.append([nums[i],nums[left],nums[right]]) 
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1

        return ans