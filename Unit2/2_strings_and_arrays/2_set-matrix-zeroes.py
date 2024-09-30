class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        R={}
        C={}

        for r in range(ROWS):
            R[r]=1
        for c in range(COLUMNS):
            C[c]=1
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if matrix[r][c]==0:
                    R[r]=0
                    C[c]=0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if R[r]==0 or C[c]==0:
                    matrix[r][c]=0
        return matrix
