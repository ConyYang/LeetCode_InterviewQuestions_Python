class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1

        while (lo <= hi):
            print(lo)
            print(hi)
            mid = lo + int((hi - lo) / 2)
            val = self.getValueByIndex(matrix, mid)
            if val == target:
                return True

            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    def getValueByIndex(self, matrix, idx):
        row = len(matrix[0])
        col = len(matrix)
        targetRow = int(idx / row)
        targetCol = int(idx % row)
        return matrix[targetRow][targetCol]