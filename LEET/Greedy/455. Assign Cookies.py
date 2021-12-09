#https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        cookie_index, child_index = 0, 0
        
        while True:
            if cookie_index >= len(s) or child_index >= len(g):
                break
            
            if s[cookie_index] >= g[child_index]:
                child_index+=1
            
            cookie_index+=1
        
        return child_index