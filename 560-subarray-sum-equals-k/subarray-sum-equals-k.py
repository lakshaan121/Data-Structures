class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1={0:1}
        sum1=0
        ans=0
        for i in range(len(nums)):
            nums[i]+=sum1
            if nums[i]-k in dict1:
                ans+=dict1[nums[i]-k]
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
            sum1=nums[i]
        return ans
        
        




        
        