class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0]) # of the first row

        r ,c = 0, num_of_columns - 1
        while r < num_of_rows and c>=0:
    
            if matrix[r][c] < target:
                 r += 1
            elif matrix[r][c] > target:
                 c -= 1
            else: 
                 return True

        return False