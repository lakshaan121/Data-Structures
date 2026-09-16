class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder=[0]*len(nums)
        sum1=0
        dict1={0:-1}
        for i in range(len(nums)):
            nums[i]+=sum1
            remainder[i]=nums[i]%k
            if remainder[i] not in dict1:
                dict1[remainder[i]]=i
            else:
                if i-dict1[remainder[i]]>=2:
                    return True
                else:
                    continue
            sum1=nums[i]
        return False


