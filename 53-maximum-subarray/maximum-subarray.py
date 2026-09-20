class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix=0
        sum1=0
        max_sum=float('-inf')
        for i in range(len(nums)):
            nums[i]+=sum1
            
            max_sum=max(max_sum,nums[i]-min_prefix)
            if nums[i]<min_prefix:
                min_prefix=nums[i]
            sum1=nums[i]
        return max_sum
