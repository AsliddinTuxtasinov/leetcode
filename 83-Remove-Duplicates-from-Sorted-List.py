from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        for item in head:
            if item not in res:
                res.append(item)
        return res


nums = [1,1,2,3,3]
print(f"head = [1,1,2,3,3]: {Solution().deleteDuplicates(head=nums)}")