class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag=True
        if n==0:
            return False
        if n<=0:
            return False
        n=abs(n)
        for i in range(32):
            if (n&(1<<i)) and flag:
                flag=False
            elif (n&(1<<i)) and not flag:
                return False
        return True