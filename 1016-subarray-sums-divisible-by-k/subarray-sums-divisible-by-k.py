class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        dict1={0:1}
        ans=0
        prefix=[0]*len(nums)
        rem=[0]*len(nums)
        sum1=0
        for i in range(len(nums)):
            nums[i]+=sum1
            rem[i]=nums[i]%k
            prefix[i]=nums[i]
            sum1=nums[i]
        for r in rem:
            if r not in dict1:
                dict1[r]=1
            else:
                ans+=dict1[r]
                dict1[r]+=1
        return ans        