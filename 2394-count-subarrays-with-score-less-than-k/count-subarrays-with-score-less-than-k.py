class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        def helper(k):
            left=0
            score=0
            sum1=0
            count=0
            for right in range(len(nums)):
                sum1+=nums[right]
                score=sum1*(right-left+1)
                while score>k:
                    sum1-=nums[left]
                    left+=1
                    score=sum1*(right-left+1)
                print(score)
                count+=right-left+1
            return count
        return helper(k-1)