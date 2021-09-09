#https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        temp=str(bin(n))
        for i in range(len(temp)):
            if temp[i]=='1':
                ans+=1
        
        return ans