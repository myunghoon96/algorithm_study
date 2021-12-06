#https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        counter = Counter(s)
        stack = []

        for char in s:
            counter[char]-=1
            
            if char in stack:
                continue
             
            while stack and stack[-1] > char and counter[stack[-1]]>=1:
                stack.pop()
                
            stack.append(char)
                        
        return ''.join(stack)