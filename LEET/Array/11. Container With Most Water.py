#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area=0
        left=0
        right=len(height)-1
        
        while right>left:

            w=right-left
            h=min(height[left], height[right])
            area=max(area, w*h)
            # print(left, right, w, h, area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return area
