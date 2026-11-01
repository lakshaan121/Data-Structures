class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        left=0
        right=1
        result=[]
        while right<len(nums):
            m=int(str(nums[left])+str(nums[right]))
            result.append(m)
            left+=2
            right+=2
        return min(result)