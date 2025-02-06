class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.append([row,col])


        for point in zeros:
            print(point)
            x,y = point[0],point[1]

            matrix[x] = [0] * (len(matrix[0]))

            for i in range(len(matrix)):
                matrix[i][y] = 0

        return matrix

        