#https://leetcode.com/problems/combination-sum/

class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(tempSum, path, start_idx):

            if tempSum > target:
                return
            
            if tempSum == target:
                answer.append(list(path))
                return
            
            for i in range(start_idx, len(candidates)):
                path.append(candidates[i])
                dfs(sum(path), path, i)
                path.pop()
            
                
        dfs(0,[],0)
        return answer

