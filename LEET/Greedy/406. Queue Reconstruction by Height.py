#https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda x:(x[0],-x[1]), reverse=True)
        
        # print(people)
        result = []
        # print()
        for h,k in people:
            result.insert(k, [h,k])
            # print(result)
        return result