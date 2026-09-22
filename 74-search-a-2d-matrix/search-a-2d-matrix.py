class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=n*m-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            coloumn=mid%n
            if matrix[row][coloumn]==target:
                return True
            elif matrix[row][coloumn]>target:
                right=mid-1
            elif matrix[row][coloumn]<target:
                left=mid+1
        return False