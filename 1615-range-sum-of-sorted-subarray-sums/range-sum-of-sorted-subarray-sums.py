class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sum1=0
        sum2=[]
        for i in range(len(nums)):
            temp=0
            for j in range(i,len(nums)):
                temp+=nums[j]
                sum2.append(temp)
        sum2.sort()
        left=left-1
        right=right-1
        sum3=sum(sum2[left:right+1])
        return sum3%(10**9+7)