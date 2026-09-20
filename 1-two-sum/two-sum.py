from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1=dict(Counter(nums))
        for i in range(len(nums)):
            if target-nums[i] in dict1 and (nums.index(target-nums[i])!=i):
                return [i,nums.index(target-nums[i])]