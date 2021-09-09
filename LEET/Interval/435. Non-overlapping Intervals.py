#https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        prevEnd = intervals[0][1]
        ans=0
        for i in range(1, len(intervals)):
            curL, curR = intervals[i]
            #overlap
            if prevEnd > curL:
                ans+=1
            else:
                prevEnd = curR

        return ans
                