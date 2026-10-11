class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum1=0
        n=len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                sum1+=(nums[i-1]**2)
                print(i)
        return sum1