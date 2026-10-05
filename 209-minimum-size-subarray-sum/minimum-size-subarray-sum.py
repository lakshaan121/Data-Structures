class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        sum1=nums[0]
        if sum1>=target:
            return 1
        min_len=float('inf')
        for right in range(1,len(nums)):
            sum1+=nums[right]
            print(sum1)
            while sum1>target:
                if sum1-nums[left]<target:
                    break
                sum1-=nums[left]
                left+=1
            if sum1>=target:
                min_len=min(min_len,right-left+1)
        if min_len==float('inf'):
            return 0
        return min_len
