#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        d = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        if len(s)%2 != 0:
            return False
        
        for char in s:
            if char in d.keys():
                stack.append(char)
                # print("open ", char)
            elif char in d.values():
                # print("close ", char)
                if not stack:
                    return False
                
                last_open = stack.pop()
                if char != d[last_open]:
                    return False
        
        if stack:
            return False
        
        return True