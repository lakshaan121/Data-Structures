class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        l = 0
        r = len(nums1) - 1
        new = []
        while l < r:
            result = nums1[l] + nums1[r]
            if result == target:
                n = nums.index(nums1[l])
                s = nums.index(nums1[r]) if nums1[l] != nums1[r] else nums.index(nums1[r], n + 1)
                new.append(n)
                new.append(s)
                break
            elif result < target:
                l += 1
            else:
                r -= 1
        return new
