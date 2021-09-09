#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=set(nums)
        ans=0
        cnt=0
        
        for n in nums:
            if n-1 not in nums:
                cnt=1
                while n+1 in nums:
                    cnt+=1
                    n+=1
            
            ans = max(ans, cnt)
            
        return ans