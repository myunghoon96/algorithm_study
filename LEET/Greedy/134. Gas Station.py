#https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start, fuel = 0, 0
        total_sum = 0
        for i in range(len(gas)):
            total_sum += (gas[i]-cost[i])
            fuel+=gas[i]-cost[i]
            
            if fuel < 0:
                start = i + 1
                fuel = 0                
                
        if start <= len(gas)-1 and total_sum >= 0:
            return start
        
        return -1