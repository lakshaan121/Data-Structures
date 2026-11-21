class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        nums=sorted([a,b,c])
        x,y,z=nums
        if z>x+y:
            return y
        else:
            return z-x
        