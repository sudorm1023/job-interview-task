#!/usr/bin/env python3

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers)-1
        while low < high:
            middle = low + (high - low) // 2
            if numbers[middle] < numbers[high]:
                high = middle
            elif numbers[middle] > numbers[high]:
                low = middle + 1
            else:
                high -= 1
            
        return numbers[low]