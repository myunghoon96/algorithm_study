#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        char_index = dict()
        ans = 0

        for right, char in enumerate(s):
           
            if char in char_index and left <= char_index[char]:
                left = char_index[char]+1

            else:
                ans = max(ans, right-left+1)

            char_index[char] = right    
            
            
        return ans
            
        