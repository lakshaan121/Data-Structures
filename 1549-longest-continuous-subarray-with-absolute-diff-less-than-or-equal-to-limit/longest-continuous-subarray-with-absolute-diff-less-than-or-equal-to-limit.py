class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        left = 0
        max_len = 0
        min_list = []
        max_list = []
        for right in range(len(nums)):
            while min_list and nums[min_list[-1]]>nums[right]:
                min_list.pop()
            min_list.append(right)
            while max_list and nums[max_list[-1]]<nums[right]:
                max_list.pop()
            max_list.append(right)
            while (nums[max_list[0]]-nums[min_list[0]]>limit):
                if min_list[0]==left:
                    min_list.pop(0)
                if max_list[0]==left:
                    max_list.pop(0)
                left+=1
            max_len=max(right-left+1,max_len)
        return max_len