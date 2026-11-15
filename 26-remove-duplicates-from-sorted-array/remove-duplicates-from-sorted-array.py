class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        a=[]
        for i in range(len(nums)):
            seen=nums[i]
            if seen not in a:
                a.append(seen)
            else:
                continue
        for i in range(len(a)):
            nums[i]=a[i]
            j+=1
        return j




        