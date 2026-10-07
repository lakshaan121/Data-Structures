class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        left=0
        right=1
        count=0
        while right<len(nums):
            diff=nums[right]-nums[right-1]
            while right+1<len(nums) and nums[right+1]-nums[right]==diff:
                right+=1
                count+=right-left-1
            left=right
            right+=1
            
        return count
        