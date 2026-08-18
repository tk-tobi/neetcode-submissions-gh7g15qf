class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        
        top_p = 0
        bottom_p = COL - 1

        while top_p <= bottom_p:
            matrix_middle = (top_p + bottom_p) // 2

            if target < matrix[matrix_middle][0]:
                bottom_p = matrix_middle - 1
            elif target > matrix[matrix_middle][-1]:
                top_p = matrix_middle + 1
            else:
                break
        if not (top_p <= bottom_p):
            return False
        
        e_middle = (top_p + bottom_p) // 2
        l, r = 0, COL - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[e_middle][m]:
                l = m + 1
            elif target < matrix[e_middle][m]:
                r = m - 1
            else:
                return True
        return False
