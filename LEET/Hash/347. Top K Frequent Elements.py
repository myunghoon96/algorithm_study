#https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        ans = []

        for key,val in counter.most_common(k):
            ans.append(key)
            
        return ans