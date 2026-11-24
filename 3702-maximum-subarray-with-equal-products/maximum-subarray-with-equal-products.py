import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        product=1
        left=0
        max_len=-1
        for right in range(len(nums)):
            product*=nums[right]
            subarray=nums[left:right+1]
            while product>(math.lcm(*subarray)*math.gcd(*subarray)):
                product/=nums[left]
                left+=1
            if product==(math.lcm(*subarray)*math.gcd(*subarray)):
                max_len=max(max_len,right-left+1)
        return max_len
