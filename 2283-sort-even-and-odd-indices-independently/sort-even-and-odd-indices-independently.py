class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even=[]
        odd=[]
        j=0
        k=0
        result=[-1]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        for i in range(len(result)):
            if i%2==0:
                result[i]=even[j]
                j+=1
            else:
                result[i]=odd[k]
                k+=1
        return result
            
        