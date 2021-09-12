#!/usr/bin/env python3

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return numbers[0]
        
        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                return numbers[i+1]
        
        return numbers[0]