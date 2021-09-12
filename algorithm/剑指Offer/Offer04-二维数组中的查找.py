#!/usr/bin/env python3

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, clomns = len(matrix), len(matrix[0])

        row, clomn = 0, clomns-1

        while row < rows and clomn >= 0:
            if matrix[row][clomn] == target:
                return True
            elif matrix[row][clomn] > target:
                clomn -= 1
            else:
                row += 1

        return False