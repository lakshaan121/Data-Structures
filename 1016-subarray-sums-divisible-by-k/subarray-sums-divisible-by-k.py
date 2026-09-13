class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        dict1={0:1}
        ans=0
        sum1=0
        for i in range(len(nums)):
            nums[i]+=sum1
            remainder=nums[i]%k
            if remainder  in dict1:
                ans+=dict1[remainder]
                dict1[remainder]+=1
            else:
                dict1[remainder]=1               
            sum1=nums[i]
        return ans

        