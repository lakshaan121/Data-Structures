class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix=[-1]*len(nums)
        dict1={0:1}
        sum1=0
        count=0
        for i in range(len(nums)):
            nums[i]+=sum1
            if nums[i]-goal in dict1:
                count+=dict1[nums[i]-goal]
            if nums[i] not in dict1:
                dict1[nums[i]]=1
            else:
                dict1[nums[i]]+=1
            sum1=nums[i]
            
        print(dict1)
        print(prefix)
        return count
