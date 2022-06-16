# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [1]*len(matrix)
        col = [1]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(len(row)):
           if row[i] == 0:
                matrix[i] = [0]*len(col)

        for j in range(len(col)):
           if col[j] == 0:
               for i in range(len(row)):
                    matrix[i][j] = 0