class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        ans=[]
        right=len(nums)-1
        for i in range(len(nums)):
            ans.append(product)
            product=nums[i]*product
        print(ans)
        product=1
        while right>=0:
            ans[right]=ans[right]*product
            product*=nums[right]
            right-=1

            
        return ans


        