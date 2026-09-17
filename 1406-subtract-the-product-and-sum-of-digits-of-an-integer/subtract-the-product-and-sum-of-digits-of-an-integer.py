class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str1=str(n)
        sum1=0
        product=1
        for i in str1:
            sum1+=int(i)
            product*=int(i)
        return product-sum1
