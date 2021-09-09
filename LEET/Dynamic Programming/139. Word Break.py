#https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True
        
        for i in range(len(s)):
            for w in wordDict:
                if dp[i]==True and i+len(w) <= len(s) and s[i:i+len(w)]==w:
                    # print(i, w, i+len(w))
                    dp[i+len(w)]=True
                
        return(dp[-1])