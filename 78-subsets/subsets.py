class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mask=0
        temp=[]
        result=[]
        n=len(nums)
        for mask in range(2**n):
            temp=[]
            for i in range(n):
                if mask & (1<<i):
                    temp.append(nums[i])

            result.append(temp)
        return result

        