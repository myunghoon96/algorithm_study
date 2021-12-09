#https://leetcode.com/problems/binary-search/

from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

#         left = bisect_left(nums,target)
#         right = bisect_right(nums,target)
#         if right-left != 0:
#              return left
            
#         return -1

        left, right = 0, len(nums)-1

        while left <= right:
            mid=left+(right-left)//2    
            if nums[mid]==target:
                return mid
                        
            if nums[mid]<target:
                left = mid+1
            
            elif nums[mid]>target:
                right=mid-1
                
        return -1
            