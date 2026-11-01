class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        sort1=nums.copy()
        count=0
        swapped=False
        sort1.sort()
        k1=0
        print(sort1)
        left=0
        right=0
        print(nums)
        for i in range(len(nums)-1):
            swapped=False
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    if locked[j]!=1 and locked[j+1]!=1:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                        count+=1
                        swapped=True
                    elif locked[j]==1 and locked[j+1]!=1:
                        if k1>=k:
                            return -1
                        else:
                            k1+=1
                            locked[j]=0
                            nums[j],nums[j+1]=nums[j+1],nums[j]
                            count+=1
                            swapped=True
                    elif locked[j]!=1 and locked[j+1]==1:
                        if k1>=k:
                            return -1
                        else:
                            k1+=1
                            locked[j+1]=0
                            nums[j],nums[j+1]=nums[j+1],nums[j]
                            count+=1
                            swapped=True
                    elif locked[j]==1 and locked[j+1]==1:
                        if k1>=k-1:
                            return -1
                        else:
                            k1+=2
                            locked[j]=0
                            locked[j+1]=0
                            nums[j],nums[j+1]=nums[j+1],nums[j]
                            count+=1
                            swapped=True
            if not swapped :
                break
        if nums==sort1:
            return count+k1
        return -1