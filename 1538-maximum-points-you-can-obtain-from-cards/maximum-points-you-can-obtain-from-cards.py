class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left=0 
        min_val=float('inf')
        sum1=0
        sum2=0
        n=len(cardPoints)
        for right in range(len(cardPoints)):
            sum1+=cardPoints[right]
            sum2+=cardPoints[right]
            while right-left+1 >n-k:
                sum1-=cardPoints[left]
                left+=1
            if right-left+1 ==n-k:
                min_val=min(min_val,sum1)
        return sum2-min_val