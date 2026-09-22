class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        m=len(matrix)
        n=len(matrix[0])
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        left=0
        top=0
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                result.append(matrix[top][j])
            top+=1
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom-=1
            if left<=right:
                for k in range(bottom,top-1,-1):
                    result.append(matrix[k][left])
                left+=1
            
        return result
