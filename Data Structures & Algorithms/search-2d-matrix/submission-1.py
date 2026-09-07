class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        start_r = 0
        end_r = m-1
        
        while start_r <= end_r:            
            mid_r = (start_r + end_r) // 2
            
            if matrix[mid_r][0] <= target <= matrix[mid_r][n-1]:
                start, end = 0, n-1
                while start <= end:
                    mid = (start + end) // 2

                    if matrix[mid_r][mid] == target:
                        return True
                    elif matrix[mid_r][mid] > target:
                        end = mid - 1
                    elif matrix[mid_r][mid] < target:
                        start = mid + 1
                return False

            elif target < matrix[mid_r][0]:
                end_r = mid_r - 1
            elif target > matrix[mid_r][0]:
                start_r = mid_r+1 

        return False