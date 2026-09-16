class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        main_count=0
        count=0
        while left<right:
            mid=(left+right)//2
            main_count=0
            count=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    count+=1
                    if count==k:
                        main_count+=1
                        count=0
                else:
                    count=0
            if main_count>=m:
                right=mid
            else:
                left=mid+1
        return left
            
                



            
                
