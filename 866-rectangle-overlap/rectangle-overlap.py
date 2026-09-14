class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1=rec1[0]
        x2=rec1[2]
        y1=rec1[1]
        y2=rec1[3]
        a1=rec2[0]
        a2=rec2[2]
        b1=rec2[1]
        b2=rec2[3]
        return not (x2 <= a1 or a2 <= x1 or y2 <= b1 or b2 <= y1)
        