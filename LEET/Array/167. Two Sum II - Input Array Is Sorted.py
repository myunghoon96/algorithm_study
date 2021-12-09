#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        
        for i,num in enumerate(numbers):
            
            if d[target-num] != 0:
                return [d[target-num],i+1]
            
            d[num]=i+1