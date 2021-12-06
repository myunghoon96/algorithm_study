#https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
               
        for i in range(len(temperatures)):
            cur_temperature = temperatures[i]

            while stack and cur_temperature > temperatures[stack[-1]]:
                node_index = stack.pop()
                answer[node_index] = i - node_index

            stack.append(i)

                    
        return answer