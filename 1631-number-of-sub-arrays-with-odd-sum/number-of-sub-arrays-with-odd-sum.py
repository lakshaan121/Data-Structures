class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        dict1={0:1}
        dict2={0:0}
        sum1=0
        count=0
        for i in range(len(arr)):
            sum1+=arr[i]
            if sum1%2==0:
                count+=dict2[0]
                dict1[0]+=1
            else:
                count+=dict1[0]
                dict2[0]+=1
        return count%(10**9+7)