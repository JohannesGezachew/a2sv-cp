class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for row in range(1,len(matrix)):
            collen = len(matrix[row])
            for col in range(1,collen):
                if matrix[row][col] != matrix[row-1][col - 1]:
                    return False
        return True
