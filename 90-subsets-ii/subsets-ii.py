class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        mask=0
        result=[]
        nums.sort()
        temp=[]
        set1=set()
        for mask in range(2**len(nums)):
            temp=[]
            for i in range(len((nums))):
                if mask &(1<<i):
                    temp.append(nums[i])
            if tuple(temp) not in set1:
                result.append(temp)
                set1.add(tuple(temp))
        return result
        