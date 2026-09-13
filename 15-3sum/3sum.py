from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x=nums[0]
        nums.sort()
        left=0
        i=0
        right=len(nums)-1
        result=[]
        for y in range(len(nums)):
            if y>0 and nums[y]==nums[y-1]:
                continue
            target=-nums[y]
            left=y+1
            right=len(nums)-1
            while left<right:
                sum1=nums[left]+nums[right]
                if sum1==target:
                    result.append([nums[y],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                if sum1<target:
                    left+=1
                elif sum1>target:
                    right-=1
                
        return result





        
            
