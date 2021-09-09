#https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        a,b = newInterval
        ans = []
        i=0
        
        if len(intervals)==0:
            ans.append(newInterval)
            return ans

        while i<len(intervals) and a>intervals[i][1]:
            ans.append(intervals[i])
            i+=1

        start = a
        end = b

        while i<len(intervals) and b>=intervals[i][0]:
            start=min(start, intervals[i][0])
            end=max(end, intervals[i][1])
            i+=1
            
        ans.append([start,end])

        while i<len(intervals):
            ans.append(intervals[i])
            i+=1

        return ans