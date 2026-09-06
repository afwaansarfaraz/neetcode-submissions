class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = 0
        y = len(matrix) * len(matrix[0]) - 1
        while x <= y :
            mid =(x+y)//2

            row = mid // len(matrix[0])#returns divide lumsum
            col = mid % len(matrix[0])# returns remainder

            if matrix[row][col]== target :
                return True
            elif matrix[row][col] < target:
                x = mid+1    
            else:
                y = mid-1   
            
        return False      


        