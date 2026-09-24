class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        nums.sort()
        dict1 = dict(Counter(nums))
        for i in range(len(nums)):
            if dict1[nums[i]] > 0:
                gd = k - 1
                dict1[nums[i]] -= 1
                num = nums[i]
                while gd > 0:
                    if num + 1 not in dict1 or dict1[num + 1] == 0:
                        return False

                    dict1[num + 1] -= 1
                    num += 1
                    gd -= 1
        return True
        