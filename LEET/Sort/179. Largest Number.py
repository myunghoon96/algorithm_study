#https://leetcode.com/problems/largest-number/

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comp(x, y):
            return int(str(x)+str(y)) - int(str(y)+str(x))
        
        nums.sort(key=cmp_to_key(comp), reverse=True)

        return str(int(''.join(str(num) for num in nums)))
