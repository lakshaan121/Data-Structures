class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        max_len=float('-inf')
        left=0
        sum1=0
        total=sum(nums)
        if x==0:
            return len(nums)
        for right in range(len(nums)):
            sum1+=nums[right]
            while left<=right and total-sum1<x:
                sum1-=nums[left]
                left+=1
            if total-sum1==x:
                max_len=max(max_len,right-left+1)
        if max_len==float('-inf'):
            return -1
        return len(nums)-max_len