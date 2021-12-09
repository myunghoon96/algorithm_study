#https://leetcode.com/problems/search-a-2d-matrix-ii/

from bisect import bisect_left, bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
  
        for row in matrix:
            if target in row:
                return True
        return False
        
#         for i in range(len(matrix)):

#             if matrix[i][0] > target:
#                 return False
                            
#             if matrix[i][0]==target:
#                 return True
            
#             if matrix[i][0]<target:
#                 left = bisect_left(matrix[i], target)
#                 right = bisect_right(matrix[i], target)
#                 if right-left !=0:
#                     return True
                