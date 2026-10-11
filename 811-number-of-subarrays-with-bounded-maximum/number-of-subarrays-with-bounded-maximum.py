from collections import deque
class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def helper(bound):
            max_ele=deque()
            count=0
            left1=0
            for i in range(len(nums)):
                while max_ele and (nums[i]>max_ele[-1]):
                    max_ele.pop()
                max_ele.append(nums[i])
                while left1<=i and max_ele[0]>bound:
                    if nums[left1]==max_ele[0]:
                        max_ele.popleft()
                    left1+=1
                count+=i-left1+1
            return count
        return helper(right)-helper(left-1)