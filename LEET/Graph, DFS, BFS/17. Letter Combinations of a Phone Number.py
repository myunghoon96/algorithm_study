#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }
        
        ans = []
        
        if digits == "":
            return []
        
        def dfs(index, result):
            
            if len(result) == len(digits):
                ans.append(result)
                return
                        

            for char in d[digits[index]]:
                dfs(index+1, result+char)
            
        dfs(0,"")
        return ans