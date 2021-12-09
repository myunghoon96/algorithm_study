#https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        ans = 0
        d = defaultdict(int)
        for task in tasks:
            d[task] += 1
            
        max_cnt = max(d.values())    
#         print("max_cnt", max_cnt)
        
        tasks_with_max_cnt = 0
        for key, val in d.items():
            if val == max_cnt:
                tasks_with_max_cnt+=1                
        # print("tasks_with_max_cnt", tasks_with_max_cnt)
        
        ans =  max_cnt + (max_cnt-1)*n +(tasks_with_max_cnt - 1)
        
        return max(len(tasks),ans)
        