class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        dict1={}
        s=nums
        left=0
        sum1=0
        max_sum=float('-inf')
        for right in range(len(nums)):
            sum1+=s[right]
            while left<right and s[right] in dict1:
                del dict1[s[left]]
                sum1-=s[left]
                left+=1
            dict1[s[right]]=1
            max_sum=max(max_sum,sum1)

        return max_sum
                
