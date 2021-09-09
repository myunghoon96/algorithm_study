#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        

        while start<=end:
            
            mid=start+(end-start)//2
            
            if end-start<=1:
                if nums[start]==target:
                    return start

                elif nums[end]==target:
                    return end
                else:
                    return -1
            
            #left half ascending order [1, 2, 3, 4, 5] (1, 2, 3)
            if nums[start]<nums[mid]:
                if nums[start]<=target and target<=nums[mid]:
                    end=mid
                else:
                    start=mid
            
            #right half ascending order [5, 1, 2, 3, 4] (2, 3, 4)
            else:
                if nums[mid]<=target and target<=nums[end]:
                    start=mid
                else:
                    end=mid