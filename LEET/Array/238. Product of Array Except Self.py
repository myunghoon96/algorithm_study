#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        temp = 1
        temp_list = []

        for i in range(len(nums)):
            temp_list.append(temp)
            temp*=nums[i]
                    
        temp=1
        temp_reverse_list = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            temp_reverse_list[i]=temp
            temp*=nums[i]
        
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i]=temp_list[i] * temp_reverse_list[i]

        # product=1
        # answer=[]
        # zeroCount=0
        # zeroIndex=[]
        # for i, e in enumerate(nums):
        #     if e==0:
        #         zeroCount+=1
        #         zeroIndex.append(i)
        #     else:
        #         product*=e
        
        # if zeroCount>1:
        #     answer=[0 for _ in range(len(nums))]
        
        # elif zeroCount==1:
        #     answer=[0 for _ in range(len(nums))]
        #     answer[zeroIndex[0]]=product
        
        # else:
        #     for e in nums:
        #         answer.append(product//e)
        
        return answer