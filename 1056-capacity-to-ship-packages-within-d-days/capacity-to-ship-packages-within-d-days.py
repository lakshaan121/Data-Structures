class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max1=sum(weights)
        min1=1
        left=max(weights)
        right=max1
        sum1=0
        count=1
        while left<right:
            mid=(left+right)//2
            sum1=0
            count=1
            for num in weights:
                if sum1+num<=mid:
                    sum1+=num
                else:
                    sum1=0
                    sum1+=num
                    count+=1
            if count<=days:
                right=mid
            else:
                left=mid+1
        return left
        