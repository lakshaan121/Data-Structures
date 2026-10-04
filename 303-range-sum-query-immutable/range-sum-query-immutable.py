class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum1=0
        n=len(self.nums)
        prefix=[-1]*len(self.nums)
        for i in range(n):
            sum1+=self.nums[i]
            prefix[i]=sum1
        if left==0:
            return prefix[right]
        return prefix[right]-prefix[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)