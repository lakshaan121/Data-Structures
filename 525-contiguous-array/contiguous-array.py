class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict1={0:-1}
        left=0
        count=0
        max_len=float('-inf')
        sum1=0
        prefix=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            nums[i]+=sum1
            if nums[i] not in dict1:
                dict1[nums[i]]=i
            else:
                max_len=max(max_len,i-dict1[nums[i]])
            prefix[i]=nums[i]
            sum1=nums[i]
            
        if max_len==float('-inf'):
            return 0
        return max_len
            





        

           
        