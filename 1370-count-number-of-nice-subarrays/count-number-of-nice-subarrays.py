class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count=0
        left=0
        def helper(k):
            count=0
            odd=0
            left=0
            for right in range(len(nums)):
                if nums[right]%2!=0:
                    count+=1
                while left<=right and count>k:
                    if nums[left]%2!=0:
                        count-=1
                    left+=1
                odd+=right-left+1
            return odd
        return helper(k)-helper(k-1)
