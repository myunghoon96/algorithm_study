#https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        ans = []
        for x,y in points:
            dist = (x**2+y**2)**0.5
            distances.append((dist, x, y))
        
        distances.sort(key = lambda x:x[0])
        
        for dist,x,y in distances[:k]:
            ans.append([x,y])
            
        return ans