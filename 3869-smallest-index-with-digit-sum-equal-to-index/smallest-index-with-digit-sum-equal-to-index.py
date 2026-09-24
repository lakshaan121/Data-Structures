class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        min_index=float('inf')
        for i in range(len(nums)):
            sum1=sum(map(int,str(abs(nums[i]))))
            if i==sum1:
                return i
        return -1

        