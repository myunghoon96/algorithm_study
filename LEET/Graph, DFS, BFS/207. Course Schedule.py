#https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course, visit):
            #course ing
            if visit[course]==-1:
                return False
            #course finish
            if visit[course]==1:
                return True
            
            visit[course]=-1
            
            for pre in graph[course]:
                if dfs(pre, visit) == False:
                    return False
            
            visit[course]=1
            return True
        
        graph=[[] for _ in range(numCourses)]
        visit=[0 for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        for course in range(numCourses):
            if visit[course] == 0:
                if dfs(course, visit) == False:
                    return False
        
        return True
    
    

        