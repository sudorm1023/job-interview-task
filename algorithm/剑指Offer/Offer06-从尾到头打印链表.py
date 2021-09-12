#!/usr/bin/env python3

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        if not head:
            return ans
        
        while head:
            ans.insert(0, head.val)
            head = head.next
        
        return ans