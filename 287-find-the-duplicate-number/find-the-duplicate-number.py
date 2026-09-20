class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=1
        count=0
        right=len(nums)-1
        while left<right:
            count=0
            mid=(left+right)//2
            for i in range(len(nums)):
                if nums[i]<=mid:
                    count+=1
            if count>mid:
                right=mid
            else:
                left=mid+1
        return left       