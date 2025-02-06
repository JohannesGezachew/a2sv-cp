class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][col] = " "


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == " ":

                    for i in range(len(matrix)):
                        if matrix[i][col] != " ":
                            matrix[i][col] = 0
                        elif row == i :
                            matrix[i][col] = 0
                    for j in range(len(matrix[0])):
                        if matrix[row][j] != " ":
                            matrix[row][j] = 0
                        elif col == j :
                            matrix[row][j] = 0

        return matrix

        