class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left=1
        right=max(position)-min(position)
        while left<=right:
            mid=(left+right)//2
            count=1
            prev=position[0]
            for i in range(1,len(position)):
                if position[i]-prev>=mid:
                    count+=1
                    prev=position[i]
            if count>=m:
                left=mid+1
            else:
                right=mid-1
        return right


        