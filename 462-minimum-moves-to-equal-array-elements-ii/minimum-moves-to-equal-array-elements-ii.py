class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid1=0
        mid=0
        count=0
        count1=0
        if len(nums)%2!=0:
            mid=nums[len(nums)//2]
            for i in nums:
                count+=abs(mid-i)
            return count
        else:
            mid=nums[len(nums)//2]
            mid1=nums[(len(nums)-1)//2]
            for i in nums:
                count+=abs(mid-i)
                count1+=abs(mid1-i)
            return min(count,count1)

        return mid1