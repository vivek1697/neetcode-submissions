class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target>=matrix[i][0] and target<=matrix[i][-1]:
                find_value=self.binarySearch(matrix[i],target)
                return find_value   
        return False

    def binarySearch(self,matrix: List[int],target) -> bool:
        left = 0 
        right = len(matrix)-1
        while left <= right:
            mid = (left + right)//2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False
        