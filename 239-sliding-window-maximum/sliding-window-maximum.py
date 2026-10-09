class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_value=deque()
        left=0
        result=[]
        for right in range(len(nums)):
            while max_value and max_value[-1]<nums[right]:
                max_value.pop()
            max_value.append(nums[right])
            while right-left+1 >k:
                if nums[left]==max_value[0]:
                    max_value.popleft()
                left+=1
            if right-left+1==k:
                result.append(max_value[0])
        return result

