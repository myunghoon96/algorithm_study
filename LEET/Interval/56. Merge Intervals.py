#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        total = len(intervals)
        ans=[]
        intervals.sort()

        if total<=1:
            return intervals

        for l,r in intervals:
            #merge
            if len(ans)>0 and ans[-1][1]>=l:  
                prevL, prevR = ans[-1]
                ans[-1][1]=max(prevR, r)
              
            else:
                ans.append([l,r])

        return(ans)
        