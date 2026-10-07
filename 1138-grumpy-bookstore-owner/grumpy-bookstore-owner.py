class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        k=minutes
        left=0
        temp=0
        satisfied=0
        max_satisfied=float('-inf')
        for right in range(len(customers)):
            if grumpy[right]==0:
                satisfied+=customers[right]
            if grumpy[right]==1:
                temp+=customers[right]
            if right-left+1 > minutes:
                if grumpy[left]==1:
                    temp-=customers[left]
                left+=1
            max_satisfied=max(max_satisfied,temp)
        return max_satisfied+satisfied