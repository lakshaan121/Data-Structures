class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dict1 = {0: 1}
        ans = 0
        sum1 = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
            sum1 += nums[i]
            need = sum1 - k
            if need in dict1:
                ans += dict1[need]
            if sum1 not in dict1:
                dict1[sum1] = 1
            else:
                dict1[sum1] += 1
        return ans