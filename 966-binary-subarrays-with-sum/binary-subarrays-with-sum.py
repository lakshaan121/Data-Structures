class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        dict1={0:1}
        sum1=0
        count=0
        for i in range(len(nums)):
            nums[i]+=sum1
            print(nums[i])
            needed=nums[i]-goal
            if needed in dict1:
                count+=dict1[needed]
            if nums[i] not in dict1:
                dict1[nums[i]]=1
            else:
                dict1[nums[i]]+=1 
            sum1=nums[i]
        return count