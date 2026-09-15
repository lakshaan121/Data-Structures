class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max1=max(piles)
        n=h
        left=1
        right=max1
        while left<right:
            count=0
            mid=(left+right)//2
            for num in piles:
               count+=math.ceil(num / mid)
            if count<=h:
                right=mid
            else:
                left=mid+1
        return left








