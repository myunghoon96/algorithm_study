#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]

        if len(nums)<3:
            return answer
        
        for i in range(len(nums)):
            if i!=0 and nums[i-1]==nums[i]:
                continue
                
            left=i+1
            right=len(nums)-1
            
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                
                if total==0:

                    answer.append([nums[i], nums[left], nums[right]])


                    while left<right:
                        if nums[left]==nums[left+1]:
                            left+=1
                        else:
                            break

                    while left<right:
                        if nums[right]==nums[right-1]:
                            right-=1
                        else:
                            break

                    left+=1
                    right-=1
                            
                elif total<0:
                    left+=1

                elif total>0:
                    right-=1
        
        return answer
            
            
            