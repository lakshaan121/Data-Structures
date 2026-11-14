class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        sum=0
        max1=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            water=width*h
            max1=max(water,max1)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max1

            


