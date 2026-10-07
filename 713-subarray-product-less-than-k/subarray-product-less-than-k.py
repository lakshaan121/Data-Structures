class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        flag=False
        if len(nums)==1:
            if nums[0]>k:
                return 0
        for i in range(len(nums)):
            if nums[i]<k:
                flag=True
        if not flag:
            return 0
        if flag:
            left=0
            product=1
            count=0
            for right in range(len(nums)):
                product*=nums[right]
                while product>=k:
                    product//=nums[left]
                    left+=1
                count+=right-left+1
        return count
            
            