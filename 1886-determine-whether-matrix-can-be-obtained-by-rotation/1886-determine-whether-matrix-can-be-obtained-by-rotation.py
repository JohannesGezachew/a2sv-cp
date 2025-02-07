class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        result = [[0]*n for _ in range(n)]
        if mat == target:
            return True
        else:
            for i in range(3): 
                for row in range(n):
                    for col in range(n):
                        result[col][n-row-1] = mat[row][col]
                for row in range(n):
                    for col in range(n):
                        mat[row][col] = result[row][col]
                if target == mat:
                    return True
            return False
        