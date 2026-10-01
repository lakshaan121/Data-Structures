class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix=[-1]*len(customers)
        suffix=[-1]*len(customers)
        min_sum=float('inf')
        min_index=-1
        count1=0
        count=0
        for i in range(len(customers)):
            if customers[i]=='N':
                count+=1
            prefix[i]=count
        for j in range(len(customers)-1,-1,-1):
            if customers[j]=='Y':
                count1+=1
            suffix[j]=count1
        for i in range(len(customers)+1):
            if i==0:
                sum1=suffix[0]
            elif i==len(customers):
                sum1=prefix[-1]
            else:
                sum1=prefix[i-1]+suffix[i]
            if sum1<min_sum:
                min_sum=sum1
                min_index=i
        return min_index