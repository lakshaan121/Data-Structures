class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        count=len(prices)
        left=0
        right=1
        while right<len(prices):
            while prices[right-1]-prices[right]==1:
                right+=1
                count+=right-left-1
                if right>len(prices)-1:
                    break
            left+=1
            right=max(right,left+1)
        return count

