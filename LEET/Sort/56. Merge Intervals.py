#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        intervals.sort(key = lambda x:(x[0],x[1]))
        
        for interval in intervals:
            left, right = interval
            
            if ans and left <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], right)
                
            else:
                ans.append(interval)
                
        return ans