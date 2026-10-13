class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        nums.sort()
        print(nums)
        result=[]
        add=[]
        negative=[]
        left=0
        right=len(nums)-1
        while left<=right:
            if left==right:
                add.append(nums[right])
            else:
                add.append(nums[right])
                negative.append(nums[left])
            left+=1
            right-=1
        sum1=0
        for i in range(len(add)):
            sum1+=add[i]**2
        for i in range(len(negative)):
            sum1-=negative[i]**2
        return sum1