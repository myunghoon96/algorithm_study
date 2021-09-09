#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
                    
        start=0
        end=len(nums)-1
        
        while (start<=end):
            mid=start+(end-start)//2
            if nums[start]<=nums[end]:
                return nums[start]
            
            if nums[mid]>=nums[start]:
                start=mid+1
            
            elif nums[mid]<nums[start]:
                end=mid
        
    