class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        min1=1
        max1=max(nums)
        left=min1
        right=max1
        thresh=0
        while left<right:
            mid=(left+right)//2
            thresh=0
            for i in range(len(nums)):
                thresh+=math.ceil(nums[i]/mid)
            if thresh<=threshold:
                right=mid
            else:
                left=mid+1
        return left
        