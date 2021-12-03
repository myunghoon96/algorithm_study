#https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        
        left_index, right_index = 0, len(height)-1
        left_max, right_max = height[0], height[-1]
        
        while left_index < right_index:

            if left_max <= right_max:
                ans+=left_max-height[left_index] 
                left_index+=1
                left_max=max(left_max, height[left_index])
                
            elif left_max > right_max:
                ans+=right_max-height[right_index]
                right_index-=1
                right_max=max(right_max, height[right_index])
                
        return ans