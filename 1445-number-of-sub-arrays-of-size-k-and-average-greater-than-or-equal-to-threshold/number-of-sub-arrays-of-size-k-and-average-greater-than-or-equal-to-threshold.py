class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left=0
        right=k
        count=0
        sum1=sum(arr[left:right])
        if (sum1//k)>=threshold:
            count+=1 
        print(sum1)
        while right<len(arr):
            sum1+=arr[right]
            sum1-=arr[left]
            print(sum1)
            avg=sum1//k
            if avg>=threshold:
                count+=1
            right+=1
            left+=1
        return count



